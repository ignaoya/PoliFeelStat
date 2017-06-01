from django.shortcuts import render
from django.http import HttpResponse
from pfs.models import Article, Country
from pfs.forms import CountryForm


# Create your views here.

def index(request):
    return render(request, 'pfs/index.html')

def about(request):
    return render(request, 'pfs/about.html')

def stats1(request):

    articles = Article.objects.get(id=579)

    countries = Country.objects.filter(article_id = articles.id)
    print(articles)
    print(countries)

    context_dict = {'countries': countries, 'articles': articles}
    return render(request, 'pfs/stats1.html', context=context_dict)

def stats2(request):

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            search_term = data['search_term']
            #search_term = form
            countries = Country.objects.filter(country = search_term)
            mentions = len(countries)

            latest = Article.objects.get(urlId = countries[mentions -1].article).date
            #latest = Article.objects.get(urlId=countries[0].article).date

            articles = []
            average = 0
            avg_length = 0
            for i in countries:
                art = Article.objects.get(urlId = i.article)
                articles.append(art)
                average += Article.objects.get(urlId = i.article).feels
                avg_length += Article.objects.get(urlId = i.article).length
            average /= mentions
            average = str(round(average, 2))
            avg_length /= mentions
            avg_length = str(round(avg_length, 2))


            context_dict = {'countries':countries, 'articles':articles, 'search_term':search_term,
                            'mentions':mentions, 'latest':latest, 'average':average, 'avg_length':avg_length}
            return render(request, 'pfs/stats2.html',  context=context_dict, )

    else:
        form = CountryForm()
    return render(request, 'pfs/stats2.html', {'form': form})