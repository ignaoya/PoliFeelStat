from django.shortcuts import render
from django.http import HttpResponse
from pfs.models import Article


# Create your views here.

def index(request):
    return render(request, 'pfs/index.html')

def about(request):
    return render(request, 'pfs/about.html')

def stats1(request):

    country_list = Article.objects.order_by('-date')[:10]
    singlecun = country_list
    context_dict = {'countries': country_list, 'single': singlecun}
    return render(request, 'pfs/stats1.html', context=context_dict)