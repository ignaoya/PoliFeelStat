##Este script busca entradas repetidas en la BD Article y los elimina
#No se por que, pero cada tanto aparecen articulos repetidos, y eso arruina toodo,
#porque la funcion get() del ORM usada en STATS 2 depende de que haya solo 1 elemento a recuperar.
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


all = Article.objects.all()
list_url = []
print(len(all))
with open ("text.txt", "w") as f:
    for i in all:
        if i.urlId  not in list_url:
            list_url.append(i.urlId)
        else:
            f.write(str(i.id))
            f.write(i.urlId)
            f.write('\n')
            Article.objects.get(id = i.id).delete()
f.closed







