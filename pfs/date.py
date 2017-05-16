##script to update all the dates on the articles, because we hadn't implemented this feature when we first created the DB.
#No need to run this anymore, already done.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pfs.models import Article

art = Article.objects.all() #load all database entries into art
for x in art:
    url = x.urlId #get the url for each art
    html = urlopen(url) #turn it into BS object
    bsObj = BeautifulSoup(html)
    date = bsObj.time.attrs['datetime'][:10]#retrieve date from page
    x.date = date #update date onto database entry
    x.save() #fucken save!

