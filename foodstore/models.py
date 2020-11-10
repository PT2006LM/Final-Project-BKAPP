from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    thumbnail = models.ImageField()
    description = models.TextField()
    status = models.IntegerField()
    ship = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    coupon = models.FloatField()
    total_price = models.FloatField()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()