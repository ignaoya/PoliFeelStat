from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.yahoo.com/news/world/")
bsObj = BeautifulSoup(html.read())
with open('newslinks.txt', 'w') as f:
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            f.write(link.attrs['href'])
            f.write('\n')
f.closed
