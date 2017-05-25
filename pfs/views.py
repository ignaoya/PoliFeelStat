from django.shortcuts import render
from django.http import HttpResponse
from pfs.models import Article, Country


# Create your views here.

def index(request):
    return render(request, 'pfs/index.html')

def about(request):
    return render(request, 'pfs/about.html')

def stats1(request):

    articles = Article.objects.get(id=579)
    #flag = []
    #lag.append(Country.objects.filter(article_id = countries.id))
    countries = Country.objects.filter(article_id = articles.id)
    print(articles)
    print(countries)

    context_dict = {'countries': countries, 'articles': articles}
    return render(request, 'pfs/stats1.html', context=context_dict)
