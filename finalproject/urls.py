"""gameshopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from finalproject import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.homepage, name='home'),
    path('test/', views.homepage, name='test-home'),
    path('test/shop-grid/', views.shop_grid, name='test-shop-grid'),
    path('test/shoping-cart/', views.shoping_cart, name='test-shoping-cart'),
    path('test/shop-details/', views.shop_detail, name='test-shop-detail'),
    path('test/contact/', views.contact, name='test-contact'),
    path('test/checkout/', views.checkout, name='test-checkout'),
    path('test/blog/', views.blog, name='test-blog'),
    path('test/blog-details/', views.blog_details, name='test-blog-details'),

    path('store/', include('foodstore.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
