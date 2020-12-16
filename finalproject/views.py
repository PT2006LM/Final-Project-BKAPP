from django.shortcuts import render
from foodstore import models
from django.core.paginator import Paginator

def homepage(request):
    product = models.Product.objects.all()
    product1 = models.Product.objects.order_by('-date_created')[:3]
    toprated = models.Product.objects.order_by('-rating')[:3]
    sales = models.Product.objects.order_by('amount')[:3]

    category = models.Category.objects.all()

    paginator = Paginator(product, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {
        'heading_menu': 'home',
        'page_obj':page_obj,
        'product1':product1,
        'toprated':toprated,
        'sales':sales,
        'category':category
    })

def contact(request):
    return render(request, 'contact.html')