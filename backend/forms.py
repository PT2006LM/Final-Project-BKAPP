from django import forms
from foodstore import models
from django.contrib.auth.models import User

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
class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(label='Tên đăng nhập', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label= 'Địa chỉ email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label= 'Mật khẩu', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    is_superuser = forms.BooleanField(label='Supper user', required=False)
    is_staff = forms.BooleanField(label='Tài khoản cấp nhân viên', required=False)
    is_active = forms.BooleanField(label='Hoạt động', required=False)
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'is_staff', 'is_active'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError('Email này đã được sử dụng')
        return email

class UserRegisterFormHome(forms.ModelForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(label='Tên đăng nhập', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Địa chỉ email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email này đã được sử dụng')
        return email
