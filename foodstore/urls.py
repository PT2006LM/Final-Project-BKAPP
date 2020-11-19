from django.urls import path
from foodstore import views
from foodstore.views import product_views, cart_views, checkout_views


urlpatterns = [
    # path('products/', views.products, name='products-grid'),
    path('products/', product_views.ProductList.as_view(), name='products'),
    path('products/<str:category>/', 
        product_views.ProductList.as_view(), 
        name='products-by-category'),
    path('products/<slug:category>/<int:pk>/', 
        product_views.product_detail, 
        name='product-detail'),
    path('cart/', cart_views.cart, name='cart-detail'),
    path('checkout/', checkout_views.checkout, name='checkout'),

    path('products/<slug:category>/<int:product_id>/set-favorite/', 
        product_views.set_favorite_product,
        name='product-set-favorite'),

]