from urllib.request import urlopen
from bs4 import BeautifulSoup

def analyze(URL, txt):
    html = urlopen(URL)
    bsObj = BeautifulSoup(html)
    pureText = bsObj.findAll("p", {"type":"text"})
    with open (txt, "w") as f:
        for tex in pureText:
            f.write(tex.attrs['content'])
            f.write('\n')
            f.write('\n')
    f.closed
