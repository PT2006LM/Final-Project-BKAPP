from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from foodstore import models



class ProductList(ListView):
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.product_count
        if self.request.method == 'GET':
            print(self.request.GET.keys())
        return context


    def paginate_queryset(self, queryset, page_size):
        try:
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        except KeyError:
            pass
        self.product_count = queryset.count()
        return super().paginate_queryset(queryset, page_size)


def products(request):
    return render(request, 'foodstore/shop-grid.html')


class ProductDetail(DetailView):
    template_name = 'foodstore/shop-details.html'
    model = models.Product


def set_favorite_product(request, category, product_id):
    # Get a Product instance with id from database
    # Add Product instance if its id not existed in session
    # Remove Product instance if it's already existed
    print(request.GET)
    try:
        favorite_products = request.session['favorite_products']
    except KeyError:
        favorite_products = {
            'length': 0,
            'object_ids': []
        }
    queried_products = list(filter(lambda product : product == product_id, 
        favorite_products['object_ids']))
    if len(queried_products) == 0:
        favorite_products['object_ids'].append(product_id)
    else:
        favorite_products['object_ids'].remove(queried_products[0])
    favorite_products['length'] = len(favorite_products['object_ids'])

    request.session['favorite_products'] = favorite_products
    return HttpResponseRedirect(reverse('product-detail', kwargs={
        'category': category,
        'pk': product_id
    }))



def cart(request):
    return render(request, 'foodstore/shoping-cart.html')


def checkout(request):
    return render(request, 'foodstore/checkout.html')