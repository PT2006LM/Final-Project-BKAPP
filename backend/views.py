from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from backend import forms
from foodstore import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class adminController:
    @login_required(login_url=reverse_lazy('backend:login'))
    def index(request):
        return render(request,'pages/index.html')

    def login(request):
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('backend:index')
        return render(request,'pages/login.html')

def register(request):
    form = forms.UserRegisterFormHome(request.POST or None)
    if form.is_valid():
        # Save form -> Create new user in database
        user = form.save()
        # Log new user in
        rawpassword = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        # Validate and get user from given credentials
        user = authenticate(username=username, password=rawpassword)
        # Finally log user in
        login(request, user)
        return redirect('home')
    return render(request, 'pages/user/register.html',{
        'form': form,
        'title': 'Register'
        })

class userController:
    def list(request):
            obj = models.User.objects.all()
            return render(request, 'pages/user/list.html', {
                'obj': obj
            })
    def register(request):
        form = forms.UserRegisterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('admin.user.list')
        return render(request, 'pages/user/register.html',{
            'form': form,
            'title': 'Admin Register'
            })
    def logout(request):
        logout(request)
        return redirect(reverse('home'))


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
            return redirect('backend:category.index')
        return render(request,'pages/category/create.html',{
            'form': form
        })
    def edit(request, id):
        obj = models.Category.objects.get(id = id)
        form = forms.CategoryForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('backend:category.index')
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
            return redirect('backend:product.index')
        return render(request,'pages/product/create.html',{
            'form': form
        })
    def edit(request, id):
        obj = models.Product.objects.get(id = id)
        form = forms.ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('backend:product.index')
        return render(request,'pages/product/edit.html',{
            'form': form
        })
    def delete(request, id):
        models.Product.objects.filter(id=id).delete()
        return redirect('backend:product.index')
    