from django.urls import path
from foodstore import views


urlpatterns = [
    # path('products/', views.products, name='products-grid'),
    path('products/', views.ListProduct.as_view(), name='products'),
    path('products/detail/', views.product_detail, name='product-detail'),
    path('cart/', views.cart, name='cart-detail'),
    path('checkout/', views.checkout, name='checkout'),
]