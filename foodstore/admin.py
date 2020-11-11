from django.contrib import admin
from foodstore import models



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass