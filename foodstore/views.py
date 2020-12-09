from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.db.models import QuerySet

from foodstore import models, forms
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
        try:
            context['query_cat'] = self.kwargs['category']
            context['cat_name'] = models.Category.objects.get(
                slug=self.kwargs['category'])
        except KeyError:
            pass
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


def product_add_cart(request, category, product_id):
    form = AddItemToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart = get_cart_from_session(request)

        # Add new items
        cart.add_item_to_cart(item_id=product_id,
            amount=int(cleaned_data['quantity']))
            
        # Save cart back to session
        request.session['cart'] = cart.get_serialized_data()
        return HttpResponseRedirect(reverse('products'))
    else:
        print("Invalid")
        print(form.errors)
    

        


def product_detail(request, category, product_id):
    product = models.Product.objects.get(pk=product_id)
    template_name = 'foodstore/shop-details.html'
    
    form = AddItemToCartForm()
    review_form = forms.ReviewForm()

    # Each user can only review each product one time
    current_user_reviewed_product = len(list(
        filter(lambda review : review.user == request.user,
        product.review_set.all())
    )) > 0
    return render(request, template_name, {
        'product': product,
        'form': form,
        'review_form': review_form,
        'current_user_reviewed_product': current_user_reviewed_product
    })


def review_create(request, category, product_id):
    print(request.method)
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)

        if review_form.is_valid():
            cleaned_data = review_form.cleaned_data
            models.Review.objects.create(
                product=models.Product.objects.get(pk=product_id),
                user=request.user,
                comment=cleaned_data['comment'],
                stars=cleaned_data['rate']
            )

        else:
            print("Invalid")

        return HttpResponseRedirect(reverse('product-detail',
                kwargs={
                    'category': category,
                    'product_id': product_id
                }))