from django.shortcuts import render, redirect
from django.urls import reverse
from cart.cart import get_cart_from_session
from cart.forms import OrderForm
from cart.models import CartItem, CartOrder, Order

from foodstore.models import Product


def checkout(request):
    cart = get_cart_from_session(request)

    if request.method == 'GET':
        if cart.is_empty():
            return redirect(reverse('home'))

        cart = cart.get_serialized_data()

        # Modify serialized cart_data to form of {
        #   'product': assocaited Product object from database assocated with id,
        #   'total_price': total_price from serialized data
        # }
        
        cart_context_data = {
            'cart_data': [ {
                'product': Product.objects.get(pk=int(key)),
                'total_price': value['total_price']
            } for key, value in cart['cart_data'].items()],
            'total_price': cart['total_price']
        }

        context_data = {
            'cart': cart_context_data,
            'form': OrderForm()
        }

        return render(request, 'cart/checkout.html', 
            context=context_data)
    elif request.method == 'POST':
        cart = cart.get_serialized_data()
        # Get order data from form, cart_data from session,
        # User object from session as well => required user authentication
        # During development process, use admin account
        request_user = request.user
        form = OrderForm(request.POST)
        if form.is_valid(): 
            cleaned_data = form.cleaned_data
            # Create a CartOrder models from cart['total_price'], session's User
            cart_order = CartOrder.objects.create(
                user=request_user, total_price=float(cart['total_price'])
            )
            # Generate CartItem from cart['cart_data']'s items and above Cart
            for key, value in cart['cart_data'].items():
                CartItem.objects.create(cart_parent=cart_order,
                    product=Product.objects.get(pk=int(key)), 
                    quantity=int(value['amount']),
                    price=float(value['price']),
                    total_price=float(value['total_price']))

            # Create final Order object from CartOrder and form.cleaned_data 
            print(cleaned_data)
            Order.objects.create(
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name'],
                street=cleaned_data['street'],
                city=cleaned_data['city'],
                detail_address=cleaned_data['detail_address'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email'],
                addition_note=cleaned_data['addition_note'],
                order_data=cart_order
            )
            # Clear cart session
            del request.session['cart']
            return redirect(reverse('checkout'))
        else:
            print("Invalid")
            return render(request, 'cart/checkout.html', 
            context=context_data)