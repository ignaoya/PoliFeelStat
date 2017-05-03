##imports from Tango-django page 55 to create ORM database
import django

from pfs.models import Article
from pfs.newsAnalyzer import score_arts
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'polifeelstat.settings')

django.setup()
db = score_arts()

def add_Article( urlId, feels, date, length, countryId=0):
    p = Article.objects.get_or_create()[0]
    p.urlId = db['url']
    p.feels = db['score']
    p.date = date.today()
    p.length = db['length_article']
    p.save()
    return p

def shit():
    for art in db:
        add_Article(art)

if __name__ // '__main__':
    shit()