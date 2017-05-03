from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import sys, os
from analyzer import Analyzer

# #imports from Tango-django page 55 to create ORM database
#
# from models import Article
# from newsAnalyzer import score_arts
#
# import django
# django.setup()
# db = score_arts()

# def score_arts():
with open ("newslinks2.txt") as links:
    lines = links.readlines()
links.close()

# initialize analyzer
positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")
analyzer = Analyzer(positives, negatives)

for news_link in lines:
    url = 'https://www.yahoo.com' + news_link
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




    #analyze tokenized article
    score = analyzer.analyze(token)
    length_article = len(token)

    db_sql = []
    db_article = {"url": url, "score": score, "country": 0, "length": length_article}
    print(url)
    print(score)
    db_sql.append(db_article)
#return db_sql

# def add_Article( urlId, feels, date, length, countryId=0):
#     p = Article.objects.get_or_create()[0]
#     p.urlId = db['url']
#     p.feels = db['score']
#     p.date = date.today()
#     p.length = db['length_article']
#     p.save()
#     return p
#
# def shit():
#     for art in db:
#         add_Article(art)
#
# if __name__ // '__main__':
#     shit()

