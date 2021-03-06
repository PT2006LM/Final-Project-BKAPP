from django.urls import path
from foodstore import views
from foodstore import views


urlpatterns = [
    # path('products/', views.products, name='products-grid'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/favorite', views.product_list_favorite,
        name='product-list-favorite'),
    path('products/<str:category>/', 
        views.ProductList.as_view(), 
        name='products-by-category'),
    path('products/<slug:category>/<int:product_id>/', 
        views.product_detail, 
        name='product-detail'),
    path('products/<slug:category>/<int:product_id>/set-favorite/', 
        views.set_favorite_product,
        name='product-set-favorite'),
    path('product/<slug:category>/<int:product_id>/add-to-cart/',
        views.product_add_cart,
        name='product-add-to-cart'),
    path('products/<slug:category>/<int:product_id>/review/create',
        views.review_create,
        name='review-create'),
    path('products/<slug:category>/<int:product_id>/review/delete/<int:review_id>',
        views.review_delete,
        name='review-delete'),
    path('products/<slug:category>/<int:product_id>/review/update/<int:review_id>',
        views.review_update,
        name='review-update')
]