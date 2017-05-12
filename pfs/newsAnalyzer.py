from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import sys, os
from pfs.analyzer import Analyzer
from pfs.countryfinder import find_country

# #imports from Tango-django page 55 to create ORM database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polifeelstat.settings')

import django
django.setup()
from pfs.models import Article


def score_arts():
    with open ("newslinks2.txt") as links:
        lines = links.readlines()
    links.close()

    # initialize analyzer
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)

    for news_link in lines:
        url = 'https://yahoo.com' + news_link
        html = urlopen(url)
        bsObj = BeautifulSoup(html)
        pureText = bsObj.findAll("p", {"type":"text"})
        with open ("text.txt", "w") as f:
            for tex in pureText:
                f.write(tex.attrs['content'])
                f.write('\n')
                f.write('\n')
        f.closed

        with open ("text.txt", "r") as f:
            text = f.read()
            token = word_tokenize(text)
        f.closed

        ##To get published date use following tags(extracted from article source):
        ##<time class="date Fz(11px) D(ib) Mb(4px)" datetime="2017-05-04T17:08:13.000Z" itemprop="datePublished" data-reactid="15">May 4, 2017</time>

        #analyze tokenized article
        score = analyzer.analyze(token)
        length_article = len(token)
        countries = find_country("text.txt")

        db_sql = []
        db_article = {"url": url, "score": score, "country": countries, "length": length_article}
        print(url)
        print(score)
        db_sql.append(db_article)
        add_Article(db_article)

def add_Article(art):
    p, created = Article.objects.get_or_create(
        countryId=0,
        urlId=art["url"],
        feels=art["score"],
        length=art["length"],
        country=art["country"])

score_arts()

if __name__ == '__main__':
    score_arts()

