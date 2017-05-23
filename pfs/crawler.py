from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.yahoo.com/news/world/")
bsObj = BeautifulSoup(html.read())
with open('newslinks.txt', 'w') as f:
    for link in bsObj.findAll("a"):
        #if link.attrs['href']:
        if link.attrs['href'].endswith('html'): ##gets us links ending in 'html', which are the real news links
            f.write(link.attrs['href'])
            f.write('\n')
f.closed

