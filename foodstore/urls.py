from django.urls import path
from foodstore import views
from foodstore import views


urlpatterns = [
    # path('products/', views.products, name='products-grid'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/<str:category>/', 
        views.ProductList.as_view(), 
        name='products-by-category'),
    path('products/<slug:category>/<int:pk>/', 
        views.product_detail, 
        name='product-detail'),
    path('products/<slug:category>/<int:product_id>/set-favorite/', 
        views.set_favorite_product,
        name='product-set-favorite'),
]