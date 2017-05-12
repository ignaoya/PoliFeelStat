from django.db import models

class Article(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    urlId = models.URLField()
    feels = models.IntegerField()
    date = models.DateField
    length = models.IntegerField()
    country = models.TextField(blank=True)

    def __str__(self):
        return self.urlId