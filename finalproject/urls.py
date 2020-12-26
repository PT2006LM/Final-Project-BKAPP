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
import debug_toolbar


urlpatterns = [
    # path('__debug__/', include(debug_toolbar.urls)),
    # path('djangoadmin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.homepage, name='home'),
    path('test/contact/', views.contact, name='test-contact'),

    path('store/', include('foodstore.urls')),
    path('cart/', include('cart.urls')),
    path('', include('backend.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
