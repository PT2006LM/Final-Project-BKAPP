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
from backend import views as viewadmin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.homepage, name='home'),
    path('test/contact/', views.contact, name='test-contact'),

    path('store/', include('foodstore.urls')),
    path('cart/', include('cart.urls')),

    # admin
    path('admin', viewadmin.adminController.index , name='admin.index'),
    path('login', viewadmin.adminController.login , name='admin.login'),
    # user
    path('admin/user', viewadmin.userController.list,  name = 'admin.user.list'),
    path('admin/user/create', viewadmin.userController.register,  name = 'admin.user.register'),
    # path('admin/user/profile', views.UserController.profile, name='admin.user.profile'),
    # path('admin/user/show/<int:id>', views.UserController.show, name='admin.user.show'),
    # path('admin/login', views.UserController.login,  name = 'admin.user.login'),

    # category
    path('admin/category', viewadmin.categoryControler.index , name='admin.category.index'),
    path('admin/category/create', viewadmin.categoryControler.create , name='admin.category.create'),
    path('admin/category/edit/<int:id>', viewadmin.categoryControler.edit , name='admin.category.edit'),
    path('admin/category/delete/<int:id>', viewadmin.categoryControler.delete , name='admin.category.delete'),
    #product
    path('admin/product', viewadmin.productController.index , name='admin.product.index'),
    path('admin/product/create', viewadmin.productController.create , name='admin.product.create'),
    path('admin/product/edit/<int:id>', viewadmin.productController.edit , name='admin.product.edit'),
    path('admin/product/delete/<int:id>', viewadmin.productController.delete , name='admin.product.delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
