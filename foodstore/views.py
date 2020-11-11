from django.shortcuts import render
from django.views.generic.list import ListView
from foodstore import models



class ListProduct(ListView):
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.get_queryset().count()
        return context


def products(request):
    return render(request, 'foodstore/shop-grid.html')


def product_detail(request):
    return render(request, 'foodstore/shop-details.html')


def cart(request):
    return render(request, 'foodstore/shoping-cart.html')


def checkout(request):
    return render(request, 'foodstore/checkout.html')