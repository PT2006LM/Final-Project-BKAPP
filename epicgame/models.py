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

class SpecificationsMini(models.Model):
    os = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=20)
    graphics = models.CharField(max_length=50)
    direct = models.CharField(max_length=20)
    soundcard = models.CharField(max_length=20)
    storage = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

class SpecificationsRecom(models.Model):
    os = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=20)
    graphics = models.CharField(max_length=50)
    direct = models.CharField(max_length=20)
    soundcard = models.CharField(max_length=20)
    storage = models.CharField(max_length=50)

class Addons(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField()
    icon = models.ImageField()
    price = models.FloatField()
    develop = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    available = models.DateField()
    rating = models.PositiveIntegerField()
    tags = models.CharField(max_length=50)

    
