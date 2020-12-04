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
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.product_count
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


    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
            print("Execute all")
            print(connection.queries)
            reset_queries()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset


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