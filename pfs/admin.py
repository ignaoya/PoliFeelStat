from django.contrib import admin
from pfs.models import Article



class ArticleModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('urlId', 'feels', 'id')

        })
    )

    class Meta:
        model = Article
# Register your models here.

admin.site.register(Article)