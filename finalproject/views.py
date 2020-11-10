from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')

def shop_grid(request):
    return render(request, 'shop-grid.html')

def shop_detail(request):
    return render(request, 'shop-details.html')

def shoping_cart(request):
    return render(request, 'shoping-cart.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')