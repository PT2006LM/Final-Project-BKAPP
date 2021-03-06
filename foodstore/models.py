from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('products-by-category', kwargs={
            'category': self.slug
        })

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    rating = models.FloatField(default=0)

    STATUS_STATES = ['Empty', 'In Stock']

    def __str__(self):
        return self.name

    def get_amount_str(self):
        return f"{self.amount} {self.unit}"

    def get_status_text(self):
        return self.STATUS_STATES[self.status]

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={
            'category': self.category.slug,
            'product_id': self.pk
        })

    class Meta:
        ordering = ['-date_created']
        

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True)