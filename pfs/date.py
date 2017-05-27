##script to update all the dates on the articles, because we hadn't implemented this feature when we first created the DB.
#No need to run this anymore, already done.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pfs.models import Article, Country
from nltk.tokenize import word_tokenize
import sys, os
from pfs.countryfinder import find_country


def add_Article(art, country_list):
    p, created = Article.objects.get_or_create(
        urlId=art["url"]
        )

    add_Country(p, country_list)

def add_Country(Article, country_list):
    for i in country_list:
        p, created = Country.objects.get_or_create(
            country=i,
            article=Article

    )
art = Article.objects.all() #load all database entries into art
for x in art:
    try:
        url = x.urlId #get the url for each art
        html = urlopen(url) #turn it into BS object
        bsObj = BeautifulSoup(html)
        pureText = bsObj.findAll("p", {"type": "text"})
        with open("text.txt", "w") as f:
            for tex in pureText:
                f.write(tex.attrs['content'])
                f.write('\n')
                f.write('\n')
        f.closed

        with open("text.txt", "r") as f:
            text = f.read()
            token = word_tokenize(text)
        f.closed

        countries = find_country("text.txt")

        db_sql = []
        db_article = {"url": url}
        print(url)

        db_sql.append(db_article)
        add_Article(db_article, countries)

        x.save() #fucken save!
    except:
        pass



