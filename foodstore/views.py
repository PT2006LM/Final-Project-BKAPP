from django.shortcuts import render
from foodstore import models



def products(request):
    return render(request, 'foodstore/shop-grid.html')


def product_detail(request):
    return render(request, 'foodstore/shop-details.html')


def cart(request):
    return render(request, 'foodstore/shoping-cart.html')


def checkout(request):
    return render(request, 'foodstore/checkout.html')