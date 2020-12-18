from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


from backend import forms
from foodstore import models

class adminController:
    @login_required(login_url=reverse_lazy('login'))
    def index(request):
        admin_users = User.objects.filter(is_staff=True)
        guest_users = User.objects.filter(is_staff=False)
        products_count = models.Product.objects.count()
        category_count = models.Category.objects.count()
        return render(request,'backend/pages/index.html', {
            'admin_users': admin_users,
            'guest_users': guest_users,
            'products_count': products_count,
            'category_count': category_count,
            'section_name': 'Danh sách'
        })

    def login(request):
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    # Check user permission to redirect home page or admin
                    login(request, user)
                    if user.is_staff:
                        redirect_page = 'index'
                    else:
                        redirect_page = 'home'
                    messages.add_message(request, messages.SUCCESS,
                        "You have successfully loged in!")
                    return redirect(reverse(redirect_page))
            else:
                messages.add_message(request, messages.ERROR,
                    "Incorrect credential.")
        return render(request,'backend/pages/login.html')

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
        messages.add_message(request, messages.SUCCESS,
            "You have successfully registered")
        return redirect('home')

    return render(request, 'backend/pages/user/register.html',{
        'form': form,
        'title': 'Register'
        })

class userController:
    def list(request):
            obj = models.User.objects.all()
            return render(request, 'backend/pages/user/list.html', {
                'obj': obj
            })
    def register(request):
        form = forms.UserRegisterFormStaff(
            request.POST or None, request.FILES or None)
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
        return render(request, 'backend/pages/user/register.html',{
            'form': form,
            'title': 'Staff Register'
            })


class categoryControler:
    def index(request):
        obj = models.Category.objects.all()
        return render(request,'backend/pages/category/index.html',{
            'obj': obj,
            'section': 'category',
            'section_name': 'Category'
        })
    def create(request):
        form = forms.CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                'You have successfully created a category')
            return redirect('category.index')
        else:
            messages.add_message(request, messages.ERROR,
                'There was something wrong, please check again')
        return render(request,'backend/pages/category/create.html',{
            'form': form,
            'section': 'category',
            'section_name': 'Category'
        })
    def edit(request, id):
        obj = models.Category.objects.get(id = id)
        form = forms.CategoryForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                'You have edited a category')
            return redirect('category.index')
        else:
            messages.add_message(request, messages.ERROR,
                'There was something wrong, please check again')
        return render(request,'backend/pages/category/edit.html',{
            'form': form,
            'section': 'category',
            'section_name': 'Category'
        })
    def delete(request, id):
        models.Category.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS,
                'You have successfully deleted a category')
        return redirect('category.index')

class productController:
    def index(request):
        obj = models.Product.objects.all()
        return render(request,'backend/pages/product/index.html',
            {
                'obj': obj,
                'section': 'product',
                'section_name': 'Product'
            })
    def create(request):
        if request.method == "POST":
            form = forms.ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=True)
                print(request.FILES)
                messages.add_message(request, messages.SUCCESS,
                    'You have successfully added a product')
                return redirect('product.index')
            else:
                messages.add_message(request, messages.ERROR,
                    'There was something wrong, please check again')
                return render(request,'backend/pages/product/create.html',{
                    'form': form,
                    'section': 'product',
                    'section_name': 'Product'
                })
        else:
            form = forms.ProductForm()
            return render(request,'backend/pages/product/create.html',{
                'form': form,
                'section': 'product',
                'section_name': 'Product'
            })
    def edit(request, id):
        obj = models.Product.objects.get(id = id)
        if request.method == "POST":
            form = forms.ProductForm(request.POST, request.FILES, instance=obj)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                    'You have successfully edited a product')
                return redirect('product.index')
            else:
                messages.add_message(request, messages.ERROR,
                    'There was something wrong, please check again')
            return render(request,'backend/pages/product/edit.html',{
                'form': form,
                'section': 'product',
                'section_name': 'Product'
            })
        else:
            form = forms.ProductForm(instance=obj)
            return render(request,'backend/pages/product/edit.html',{
                'form': form,
                'section': 'product',
                'section_name': 'Product'
            })
    def delete(request, id):
        models.Product.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS,
                'You have successfully deleted a product')
        return redirect('product.index')
    