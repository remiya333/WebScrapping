import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
#print(soup.find('a'))
#print(soup.find_all(id = 'score_23972929'))
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

megalinks = links + links2
megasubtext = subtext + subtext2
#print(links[0])
def sort_stories_by_votes(hnlist):

    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            #print(points)
            if points>99:
                hn.append({'title': title, 'link': href,'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(megalinks,megasubtext))
