from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from foodstore import models, forms
from foodstore.cart import Cart, get_cart_from_session



class ProductList(ListView):
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 1
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.product_count
        return context


    def paginate_queryset(self, queryset, page_size):
        try:
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        except KeyError:
            pass
        self.product_count = queryset.count()
        return super().paginate_queryset(queryset, page_size)


def set_favorite_product(request, category, product_id):
    # Get a Product instance with id from database
    # Add Product instance if its id not existed in session
    # Remove Product instance if it's already existed
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

        form = forms.AddItemToCartForm(request.POST)
        if form.is_valid():
            cart = get_cart_from_session(request)

            # Add new items
            cart.add_item_to_cart(item_id=form.data['product_id'],
                        amount=int(form.data['quantity']))
            
            # Save cart back to session
            request.session['cart'] = cart.get_serialized_data()

            return HttpResponseRedirect(reverse('products'))

    elif request.method == 'GET':
        form = forms.AddItemToCartForm()
        return render(request, template_name, {
            'product': product,
            'form': form
        })
        



def cart(request):
    cart = get_cart_from_session(request)
    form_cart_items_data = {}

    if request.method == "POST":
        for key in cart.cart_data:
            form_cart_items_data[key] = cart.cart_data[key]['amount']
        form = forms.CartEditForm(extra=form_cart_items_data)
        form.data = request.POST
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            total_price = cleaned_data.pop('total_price')
            for key, value in cleaned_data:
                print(key)
                if "productamount_" in key:
                    print(value)
            return HttpResponseRedirect(reverse('cart-detail'))
        else:
            print("Not valid")


    elif request.method == "GET":
        
        cart_data = []
        
        for key in cart.cart_data:
            cart_data.append({
                'amount': cart.cart_data[key]['amount'],
                'total_price': cart.cart_data[key]['total_price'],
                'product': models.Product.objects.get(pk=int(key))
            })
            form_cart_items_data["product_%s" % key] = cart.cart_data[key]['amount']
        form_cart_items_data['total_price'] = str(cart.total_price)
        form = forms.CartEditForm(data=form_cart_items_data,                extra=form_cart_items_data)
        return render(request, 'foodstore/shoping-cart.html', {
            'cart_data': cart_data,
            'form': form,
            'total_price': cart.total_price,
        })


def checkout(request):
    return render(request, 'foodstore/checkout.html')