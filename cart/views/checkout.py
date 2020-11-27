from django.shortcuts import render, redirect
from django.urls import reverse
from cart.cart import get_cart_from_session
from foodstore.models import Product


def checkout(request):
    cart = get_cart_from_session(request)

    if cart.is_empty():
        return redirect(reverse('home'))

    cart = cart.get_serialized_data()

    # Modify serialized cart_data to form of {
    #   'product': assocaited Product object from database assocated with id,
    #   'total_price': total_price from serialized data
    # }
    print(cart)
    cart_context_data = {
        'cart_data': [ {
            'product': Product.objects.get(pk=int(key)),
            'total_price': value['total_price']
        } for key, value in cart['cart_data'].items()],
        'total_price': cart['total_price']
    }

    return render(request, 'cart/checkout.html', 
        context=cart_context_data)