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
from pfs.models import Article, Country


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
        date = bsObj.time.attrs['datetime'][:10] #finds datetime attribute and prints first 10 chars (only date, no time)

        db_sql = []
        db_article = {"url": url, "score": score, "length": length_article, "date":date}


        print(url)
        print(score)
        db_sql.append(db_article)
        add_Article(db_article, countries)


def add_Article(art, country_list):
    p, created = Article.objects.get_or_create(
        urlId=art["url"],
        feels=art["score"],
        length=art["length"],
        date=art["date"])

    add_Country(p, country_list)

def add_Country(Article, country_list):
    for i in country_list:
        p, created = Country.objects.get_or_create(
            country=i,
            article=Article

    )

score_arts()

if __name__ == '__main__':
    score_arts()

