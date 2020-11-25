from django.shortcuts import render, redirect
from backend import forms
from foodstore import models
# Create your views here.

class adminController:
    def index(request):
        return render(request,'main.html')

class categoryControler:
    def index(request):
        obj = models.Category.objects.all()
        return render(request,'pages/category/index.html',{
            'obj': obj
        })
    def create(request):
        form = forms.CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('admin.category.index')
        return render(request,'pages/category/create.html',{
            'form': form
        })
    def edit(request, id):
        obj = models.Category.objects.get(id = id)
        form = forms.CategoryForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('admin.category.index')
        return render(request,'pages/category/edit.html',{
            'form': form
        })
    def delete(request, id):
        models.Category.objects.filter(id=id).delete()
        return redirect('admin.category.index')

class productController:
    def index(request):
        obj = models.Product.objects.all()
        return render(request,'pages/product/index.html',
            {'obj': obj})
    def create(request):
        form = forms.ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('admin.product.index')
        return render(request,'pages/product/create.html',{
            'form': form
        })
    def edit(request, id):
        obj = models.Product.objects.get(id = id)
        form = forms.ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('admin.product.index')
        return render(request,'pages/product/edit.html',{
            'form': form
        })
    def delete(request, id):
        models.Product.objects.filter(id=id).delete()
        return redirect('admin.product.index')
    