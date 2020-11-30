from django.db import models
from django.contrib.auth.models import User
from foodstore.models import Product




class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    # coupon = models.FloatField()
    total_price = models.FloatField()


class CartItem(models.Model):
    cart_parent = models.ForeignKey(CartOrder, on_delete=models.CASCADE, db_constraint=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_constraint=False)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return self.product.name
        

class Order(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    detail_address = models.TextField(max_length=50)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    addition_note = models.TextField(max_length=50)
    order_data = models.OneToOneField(CartOrder, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)