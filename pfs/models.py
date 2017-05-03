from django.db import models

class Article(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    countryId = models.IntegerField()
    urlId = models.URLField()
    feels = models.IntegerField()
    date = models.DateField
    length = models.IntegerField()

    def __str__(self):
        return self.urlId