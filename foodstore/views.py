from django.shortcuts import render
from django.views.generic import ListView, DetailView
from foodstore import models



class ProductList(ListView):
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.get_queryset().count()
        return context


    def paginate_queryset(self, queryset, page_size):
        try:
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        except KeyError:
            pass
        return super().paginate_queryset(queryset, page_size)


def products(request):
    return render(request, 'foodstore/shop-grid.html')


class ProductDetail(DetailView):
    template_name = 'foodstore/shop-details.html'
    model = models.Product


def product_detail(request):
    return render(request, 'foodstore/shop-details.html')


def cart(request):
    return render(request, 'foodstore/shoping-cart.html')


def checkout(request):
    return render(request, 'foodstore/checkout.html')