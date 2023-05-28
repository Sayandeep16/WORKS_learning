import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_hn(links, votes):
    hn = []
    for inx, item in enumerate(links):
        title = links[inx].getText()
        href = links[inx].get(('href', None))
        hn.append({'title': title, 'links': href})
    return hn

print(create_hn(links, votes))