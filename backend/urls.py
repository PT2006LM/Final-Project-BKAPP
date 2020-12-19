from django.urls import path
from backend import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from finalproject import settings

urlpatterns = [
    # auth
    path('login', views.adminController.login , 
        name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),
        name='logout'),
    # Password Reset Views
    path('password/reset', PasswordResetView.as_view(), 
        name="password_reset"),
    path('password/reset/done', PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"),
    path('password/reset/complete', PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),

    path('admin', views.adminController.index, 
        name='index'),
    # user
    path('admin/user', views.userController.list,  
        name='user.list'),
    path('admin/user/create', views.userController.register,
        name='user.register'),

    # category
    path('admin/category', views.categoryControler.index , 
        name='category.index'),
    path('admin/category/create', views.categoryControler.create, 
        name='category.create'),
    path('admin/category/edit/<int:id>', views.categoryControler.edit,  
        name='category.edit'),
    path('admin/category/delete/<int:id>', views.categoryControler.delete, 
        name='category.delete'),

    #product
    path('admin/product', views.productController.index, 
        name='product.index'),
    path('admin/product/create', views.productController.create, 
        name='product.create'),
    path('admin/product/edit/<int:id>', views.productController.edit, 
        name='product.edit'),
    path('admin/product/delete/<int:id>', views.productController.delete, 
        name='product.delete'),

    # orders
    path('admin/order', views.orderController.index,
        name='order.index'),
    path('admin/order/<int:id>', views.orderController.detail,
        name='order.detail'),
]