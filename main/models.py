from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    publisher = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    rating = models.IntegerField()
    release = models.IntegerField()
