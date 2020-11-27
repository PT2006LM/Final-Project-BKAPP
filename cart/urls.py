from django.urls import path
from cart.views import cart, checkout


urlpatterns = [
    path('', cart.cart, name='cart-detail'),
    path('checkout/', checkout.checkout, name='checkout'),
]