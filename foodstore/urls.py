from django.urls import path
from foodstore import views


urlpatterns = [
    # path('products/', views.products, name='products-grid'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/<str:category>/', 
        views.ProductList.as_view(), 
        name='products-by-category'),
    path('products/<str:category>/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('cart/', views.cart, name='cart-detail'),
    path('checkout/', views.checkout, name='checkout'),
]