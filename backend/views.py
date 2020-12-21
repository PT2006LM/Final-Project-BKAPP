from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.http.response import HttpResponse
from django.template import RequestContext

from weasyprint import HTML

from backend import forms
from foodstore import models
from cart import models as cart_models

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
            'section_name': 'Home'
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
            'section': 'Categories',
            'section_name': 'Categories',
            'section_parent_nav': 'Categories',
        })
    def create(request):
        if request.method == 'POST':
            form = forms.CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                    'You have successfully created a category')
                return redirect('category.index')
            else:
                messages.add_message(request, messages.ERROR,
                    'There was something wrong, please check again')
                parent_sections = {
                    'Categories': reverse_lazy('category.index'),
                }
                return render(request,'backend/pages/category/create.html',{
                    'form': form,
                    'section': 'Create',
                    'section_name': 'Categories',
                    'parent_sections': parent_sections,
                    'section_parent_nav': 'Categories',
                })
        else:
            form = forms.CategoryForm()
            parent_sections = {
                    'Categories': reverse_lazy('category.index'),
                }
            return render(request,'backend/pages/category/create.html',{
                'form': form,
                'section': 'Create',
                'section_name': 'Categories',
                'parent_sections': parent_sections,
                'section_parent_nav': 'Categories',
            })

    def edit(request, id):
        obj = models.Category.objects.get(id = id)
        if request.method == 'POST':
            form = forms.CategoryForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                    'You have edited a category')
                return redirect('category.index')
            else:
                messages.add_message(request, messages.ERROR,
                    'There was something wrong, please check again')
                parent_sections = {
                    'Categories': reverse_lazy('category.index'),
                }
                return render(request,'backend/pages/category/edit.html',{
                    'form': form,
                    'section': 'Edit_' + str(id),
                    'section_name': 'Categories',
                    'parent_sections': parent_sections,
                    'section_parent_nav': 'Categories',
                })
        else:
            form = forms.CategoryForm(instance=obj)
            parent_sections = {
                'Categories': reverse_lazy('category.index'),
            }
            return render(request,'backend/pages/category/edit.html',{
                'form': form,
                'section': 'Edit_' + str(id),
                'section_name': 'Categories',
                'parent_sections': parent_sections,
                'section_parent_nav': 'Categories',
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
                'section': 'Products',
                'section_name': 'Products',
                'section_parent_nav': 'Categories',
            })
    def create(request):
        if request.method == "POST":
            form = forms.ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=True)
                messages.add_message(request, messages.SUCCESS,
                    'You have successfully added a product')
                return redirect('product.index')
            else:
                messages.add_message(request, messages.ERROR,
                    'There was something wrong, please check again')
                parent_sections = {
                    'Products': reverse_lazy('product.index'),
                }
                return render(request,'backend/pages/product/create.html',{
                    'form': form,
                    'section': 'Create',
                    'section_name': 'Products',
                    'parent_sections': parent_sections,
                    'section_parent_nav': 'Categories',
                })
        else:
            form = forms.ProductForm()
            parent_sections = {
                    'Products': reverse_lazy('product.index'),
                }
            return render(request,'backend/pages/product/create.html',{
                'form': form,
                'section': 'Create',
                'section_name': 'Products',
                'parent_sections': parent_sections,
                'section_parent_nav': 'Categories',
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
                parent_sections = {
                    'Products': reverse_lazy('product.index'),
                }
                return render(request,'backend/pages/product/edit.html',{
                    'form': form,
                    'section': 'Edit_' + str(id),
                    'section_name': 'Products',
                    'parent_sections': parent_sections,
                    'section_parent_nav': 'Categories',
                })
        else:
            form = forms.ProductForm(instance=obj)
            parent_sections = {
                    'Products': reverse_lazy('product.index'),
                }
            return render(request,'backend/pages/product/edit.html',{
                'form': form,
                'section': 'Edit_' + str(id),
                'section_name': 'Products',
                'parent_sections': parent_sections,
                'section_parent_nav': 'Categories',
            })
    def delete(request, id):
        models.Product.objects.filter(id=id).delete()
        messages.add_message(request, messages.SUCCESS,
                'You have successfully deleted a product')
        return redirect('product.index')

class orderController:
    def index(request):
        orders = cart_models.Order.objects.select_related(
            'order_data').all()
        return render(request, 'backend/pages/order/index.html', {
            'obj': orders,
            'section': 'Orders',
            'section_name': 'Orders'
        })
    def detail(request, id):
        order = cart_models.Order.objects.select_related(
            'order_data'
        ).get(pk=id)
        parent_sections = {
            'Orders': reverse_lazy('order.index'),
        }
        return render(request, 'backend/pages/order/detail.html',
            {
                'order': order,
                'section': 'Order_' + str(id),
                'section_name': 'Orders',
                'parent_sections': parent_sections,
            })

    def update(request, id):
        order = cart_models.Order.objects.get(pk=id)
        order.paid = not order.paid
        order.save()
        messages.add_message(request, messages.SUCCESS,
            f"Order {id} updated")
        return redirect(reverse('order.index'))

    def delete(request, id):
        cart_models.Order.objects.get(pk=id).delete()
        messages.add_message(request, messages.SUCCESS,
            f"Order {id} deleted")
        return redirect(reverse('order.index'))

    def detail_pdf(request, id):
        order = cart_models.Order.objects.select_related(
            'order_data'
        ).get(pk=id)

        parent_sections = {
            'Orders': reverse_lazy('order.index'),
        }

        html_string = render_to_string('backend/pages/order/order_pdf_template.html', {
                'order': order,
                'section': 'Order_' + str(id),
                'section_name': 'Orders',
                'parent_sections': parent_sections,
            }, request=request)
        html = HTML(string=html_string)
        main_doc = html.render()
        result = main_doc.write_pdf()

        return HttpResponse(result, content_type="application/pdf")