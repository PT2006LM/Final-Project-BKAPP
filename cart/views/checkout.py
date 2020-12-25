from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.contrib.auth.decorators import login_required

from cart.cart import get_cart_from_session
from cart.forms import OrderForm
from cart.models import CartItem, CartOrder, Order
import json

from foodstore.models import Product


@login_required
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
        # Get vietnam location's data to render district and city fields
        with open('cart/vietnam_loc_data.json', 'r') as json_file:
            vietnam_loc_data = json.load(json_file)
        
        cart_context_data = {
            'cart_data': [ {
                'product': Product.objects.get(pk=int(key)),
                'total_price': value['total_price']
            } for key, value in cart['cart_data'].items()],
            'total_price': cart['total_price'],
        }

        context_data = {
            'cart': cart_context_data,
            'form': OrderForm(),
            'vietnam_loc_data': vietnam_loc_data
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
            # Clear cart session
            request.session['cart'] = {}
            del request.session['cart']
            
            cleaned_data = form.cleaned_data
            # Create a CartOrder models from cart['total_price'], session's User
            cart_order = CartOrder.objects.create(
                user=request_user, total_price=float(cart['total_price'])
            )
            
            # Generate CartItem from cart['cart_data']'s items and above Cart
            for key, value in cart['cart_data'].items():
                product = Product.objects.get(pk=int(key))
                amount = int(value['amount'])
                CartItem.objects.create(cart_parent=cart_order,
                    product=product, 
                    quantity=amount,
                    price=float(value['price']),
                    total_price=float(value['total_price']))
                # Update product sold quantity
                product.amount += amount
                product.save()

            # Create final Order object from CartOrder and form.cleaned_data 
            order = Order.objects.create(
                first_name=cleaned_data['first_name'],
                last_name=cleaned_data['last_name'],
                districts=cleaned_data['district'],
                city=cleaned_data['city'],
                detail_address=cleaned_data['detail_address'],
                phone=cleaned_data['phone'],
                email=cleaned_data['email'],
                addition_note=cleaned_data['addition_note'],
                order_data=cart_order
            )
            messages.add_message(request, messages.SUCCESS, 
                "Payment successfully! We sent an email about your order, please check your inbox.")
            send_bill_email(request, order)
            return render(request, 'cart/checkout_completed.html')
        else:
            # Modify serialized cart_data to form of {
            #   'product': assocaited Product object from database assocated with id,
            #   'total_price': total_price from serialized data
            # }
            # Get vietnam location's data to render district and city fields
            with open('cart/vietnam_loc_data.json', 'r') as json_file:
                vietnam_loc_data = json.load(json_file)
            
            cart_context_data = {
                'cart_data': [ {
                    'product': Product.objects.get(pk=int(key)),
                    'total_price': value['total_price']
                } for key, value in cart['cart_data'].items()],
                'total_price': cart['total_price'],
            }

            context_data = {
                'cart': cart_context_data,
                'form': form,
                'vietnam_loc_data': vietnam_loc_data
            }
            messages.add_message(request, messages.ERROR, 
                'Some error has occur, please try again')
            return render(request, 'cart/checkout.html', 
            context=context_data)


def send_bill_email(request, order):
    ctx = {
        'order': order
    }
    html_content = get_template('cart/order_email_template.html').render(ctx)
    mail = EmailMessage(
        subject="Your order is ready",
        body=html_content,
        from_email="localhost@mail.com",
        to=[order.email]
    )
    mail.content_subtype = "html"
    mail.send()
    print("Mail successfully sent")