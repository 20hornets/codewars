import requests
from bs4 import BeautifulSoup
import pprint

#LET .storylink = .titleline

res = requests.get('https://news.ycombinator.com/')     #url
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')[0:10]                 #soup.select(".titleline")[0:10] #code from before
votes = soup.select('.score')
subtext = soup.select('.subtext')
#attempt 1
next_page = soup.select('.morelink')
#attempt 2
#next_page = soup.select('news?p=2')
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['votes'], reverse = True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points})
        more = next_page[idx].select('news?p=2')
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))