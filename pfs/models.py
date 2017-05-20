from django.db import models

class Article(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    urlId = models.URLField()
    feels = models.IntegerField()
    date = models.DateField(blank=True)
    length = models.IntegerField()

    def __str__(self):
        return self.urlId

class Country(models.Model):
    country = models.TextField(blank = True)
    article = models.ManyToManyField(Article)

    def __str__(self):
        return self.country
