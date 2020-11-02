from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=50)
    banner = models.ImageField()
    thumbnail = models.ImageField()
    description = models.TextField()
    develop = models.CharField(max_length=50)
    publish = models.CharField(max_length=50)
    release = models.DateTimeField()
    tag = models.ChoicesField()
    rating = models.FloatField()
    aboutgame = models.TextField()
    aboutgameimg = models.ImageField()
class Specifications(models.Model):
    mire = models.CharField(max_length=50)
    
