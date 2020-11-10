from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    thumbnail = models.ImageField()
    description = models.TextField()
    status = models.IntegerField()
    ship = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)

class Reviews(models.Model):
    products = models.ForeignKey(products)
    users = models.ForeignKey(users)
    stars = models.IntegerField()
    comment = models.TextField()
class Cart(models.Model):
    users = models.ForeignKey(users)
    date_created = models.DateField()
    coupon = models.FloatField()
    total_price = models.FloatField()
class CartItems(models.Model):
    cart = models.foreignKey(cart)
    products = models.foreignKey(Products)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()