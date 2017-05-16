from django.conf.urls import url
from pfs import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^stats1/', views.stats1, name='stats1'),
]