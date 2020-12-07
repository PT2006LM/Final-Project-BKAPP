from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import QuerySet

from foodstore import models
from cart.cart import get_cart_from_session
from cart.forms import CartEditForm, AddItemToCartForm
from django.db import connection, reset_queries

class ProductList(ListView):
    """
    Views listing product including category filter
    """
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 6


    def get_ordering(self):
        """
        Setup ordering based on 'sort_by' in GET's query.
        If the parameter not found, default value used.
        """
        ordering = self.request.GET.get('sort_by', '-id')
        return ordering


    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductList, self).get_queryset(*args, **kwargs)
        # Check if queried name existed in GET
        queried_name = self.request.GET.get('q', None)
        if queried_name:
            queryset = queryset.filter(name__icontains=queried_name)
        queried_cat = self.request.GET.get('category', None)
        if queried_cat:
            queryset = queryset.filter(category_id=queried_cat)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.product_count
        context['heading_menu'] = 'product'
        ordering = self.request.GET.get('sort_by', None)
        if ordering:
            context['sort_by'] = ordering
        return context


    def paginate_queryset(self, queryset, page_size):
        """
        Process filtering
        """
        try:
            # Filter by category
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        except KeyError:
            pass
        self.product_count = queryset.count()
        return super().paginate_queryset(queryset, page_size)


    def get_template_names(self):
        mode = self.request.GET.get('mode', 'grid')
        if mode == 'list':
            self.template_name = 'foodstore/shop-list.html'
        return self.template_name


def set_favorite_product(request, category, product_id):
    """
    Get a Product instance with id from database
    Add Product instance if its id not existed in session
    Remove Product instance if it's already existed
    """
    next_url = request.GET.__getitem__('next')
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
    return HttpResponseRedirect(next_url)



def product_detail(request, category, pk):
    product = models.Product.objects.get(pk=pk)
    template_name = 'foodstore/shop-details.html'
    if request.method == 'POST':

        form = AddItemToCartForm(request.POST)
        if form.is_valid():
            cart = get_cart_from_session(request)

            # Add new items
            cart.add_item_to_cart(item_id=form.data['product_id'],
                        amount=int(form.data['quantity']))
            
            # Save cart back to session
            request.session['cart'] = cart.get_serialized_data()

            return HttpResponseRedirect(reverse('products'))

    elif request.method == 'GET':
        form = AddItemToCartForm()
        return render(request, template_name, {
            'product': product,
            'form': form
        })