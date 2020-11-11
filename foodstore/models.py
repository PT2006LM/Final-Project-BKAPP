from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='uploads/product_thumbnails/%Y/%m/%d/')
    description = models.TextField(default="Description will be updated soon")
    status = models.IntegerField(default=0)
    ship = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    unit = models.CharField(max_length=50, blank=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']

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