from django.contrib import admin
from foodstore import models

class ReviewTabularInlines(admin.TabularInline):
    model = models.Review


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewTabularInlines]

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

