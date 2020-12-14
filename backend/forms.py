from django import forms
from foodstore import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Tên danh mục', widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = models.Category
        fields = ['name']
class ProductForm(forms.ModelForm):
    name = forms.CharField(label="Tên sản phẩm", widget=forms.TextInput(attrs={'class':"form-control"}))
    price = forms.FloatField(label="Giá sản phẩm", widget=forms.TextInput(attrs={'class':"form-control"}))
    thumbnail = forms.ImageField(label="Ảnh sản phẩm", widget=forms.FileInput(attrs={'class':"form-control"}))
    description = forms.CharField(label="Nội dung sản phẩm", widget=forms.Textarea(attrs={'class':"form-control"}))
    status = forms.IntegerField(label="Trạng thái", widget=forms.NumberInput(attrs={'class':"form-control"}))
    ship = forms.CharField(label="Thời gian giao hàng", widget=forms.TextInput(attrs={'class':"form-control"}))
    amount = forms.FloatField(label="Số lượng", widget=forms.NumberInput(attrs={'class':"form-control"}))
    unit = forms.CharField(label="Đơn vị", widget=forms.TextInput(attrs={'class':"form-control"}))
    date_created = forms.DateField(label="Ngày", widget=forms.DateInput(attrs={'class':"form-control"}))
    class Meta:
        model = models.Product
        fields = '__all__'
    #['name','price','thumbnail','description','status','ship','amount','unit','date_created','category']

# User
class UserRegisterFormHome(UserCreationForm):
    first_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'First Name'
            }))
    last_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Last name'
            }))
    username = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Tên đăng nhập'
            }))
    email = forms.EmailField(label='',
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'placeholder': 'Địa chỉ email'
            }))
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Mật khẩu'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Nhập lại mật khẩu'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")
#user manager
class UserRegisterFormStaff(UserCreationForm):
    first_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'First Name'
            }))
    last_name = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Last name'
            }))
    username = forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Tên đăng nhập'
            }))
    email = forms.EmailField(label='',
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'placeholder': 'Địa chỉ email'
            }))
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Mật khẩu'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'placeholder': 'Nhập lại mật khẩu'
            }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    is_staff = forms.BooleanField(label='Quản lý',
        widget=forms.CheckboxInput(attrs={
            'class': "form-control",
            }))

    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email","is_staff")