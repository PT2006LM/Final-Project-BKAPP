from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from foodstore.models import Product
from cart.cart import Cart, get_cart_from_session
from cart.forms import CartEditForm



def cart(request):
    if request.method == "POST":
        if request.POST["submit"] == "Update Cart":
            return handle_update_cart_form(request)

    elif request.method == "GET":
        return get(request)
        


def handle_update_cart_form(request):
    """
    Generating a form with extra fields according to 
    session's cart_data, with data provied by request.POST
    """
    cart = get_cart_from_session(request)
    form_cart_items_data = {}
    for key in cart.cart_data:
        if key not in request.POST:
            continue
        form_cart_items_data[key] = cart.cart_data[key]['amount']
    form = CartEditForm(request.POST, extra=form_cart_items_data)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        # Remove total_price from cleaned_data
        cleaned_data.pop('total_price')
        cart_data = cleaned_data
        # update_cart_data also update total_price so no need to store 
        # total_price from cleaned_data
        cart.update_cart_data(cart_data)

        request.session['cart'] = cart.get_serialized_data()
        messages.add_message(request, messages.SUCCESS, 
            'Successfully updated item!')

        return HttpResponseRedirect(reverse('cart-detail'))
    else:
        messages.add_message(request, messages.ERROR, 
            'There was a problem updating the cart')
        return HttpResponseRedirect(reverse('cart-detail'))


def get(request):
    """
    Handle get method in cart views.
    Construct form based on cart_data stored in session.
    """
    cart = get_cart_from_session(request)
    form_cart_items_data = {}

    cart_rendering_data = []
        
    for key in cart.cart_data:
        cart_rendering_data.append({
            'amount': cart.cart_data[key]['amount'],
            'total_price': cart.cart_data[key]['total_price'],
            'product': Product.objects.get(pk=int(key))
        })
        form_cart_items_data[key] = cart.cart_data[key]['amount']
    form_cart_items_data['total_price'] = str(cart.total_price)
    # Init form with data provided above and construct fields based on
    # extra parameter
    form = CartEditForm(data=form_cart_items_data, 
            extra=form_cart_items_data)
        
    for cart_item in cart_rendering_data:
        product_id = str(cart_item['product'].pk)
        cart_item['form_field'] = form[product_id]

    return render(request, 'cart/shopping-cart.html', {
        'cart_data': cart_rendering_data,
        'cart_data_len': len(cart_rendering_data),
        'total_price': cart.total_price,
    })
