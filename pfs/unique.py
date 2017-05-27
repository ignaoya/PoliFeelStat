##script to update all the dates on the articles, because we hadn't implemented this feature when we first created the DB.
#No need to run this anymore, already done.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pfs.models import Article
from nltk.tokenize import word_tokenize
import sys, os
from pfs.countryfinder import find_country



art = Article.objects.all() #load all database entries into art
for x in art:
    url = x.urlId #get the url for each art
    url_list = []
    url_list.append(url)
    set([x for x in url_list if url_list.count(x)>1])

    print(set)




