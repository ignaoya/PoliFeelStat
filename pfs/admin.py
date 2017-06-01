from django.contrib import admin
from pfs.models import Article, Country



class ArticleModelAdmin(admin.ModelAdmin):
    fields = ['id', 'feels', 'urlId']

    list_display = ('id', 'feels', 'urlId')
    search_fields = ('id', 'urlId',)

    class Meta:
        model = Article

class CountryModelAdmin(admin.ModelAdmin):
    fields = ['id', 'country', 'article']

    list_display = ('id', 'country', 'article')
    search_fields = ('country',)

    class Meta:
        model = Country

# Register your models here.

admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Country, CountryModelAdmin)
