from django import forms
from foodstore import models

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