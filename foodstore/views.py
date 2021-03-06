from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.views.generic import ListView
from django.db.models import QuerySet
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, SuspiciousOperation

from foodstore import models, forms
from cart.cart import get_cart_from_session
from cart.forms import CartEditForm, AddItemToCartForm

class ProductList(ListView):
    """
    Views listing product including category filter
    """
    template_name = 'foodstore/shop-grid.html'
    model = models.Product
    paginate_by = 6


    def get_ordering(self):
        """
        Setup ordering based on 'sort_by' in GET's query.
        If the parameter not found, default value used.
        """
        ordering = self.request.GET.get('sort_by', '-id')
        return ordering


    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all().select_related('category')
        # Check if queried name existed in GET
        queried_name = self.request.GET.get('q', None)
        if queried_name:
            queryset = queryset.filter(name__icontains=queried_name)
        queried_cat = self.request.GET.get('category', None)
        if queried_cat:
            queryset = queryset.filter(category_id=queried_cat)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = self.product_count
        context['heading_menu'] = 'product'
        try:
            context['query_cat'] = self.kwargs['category']
            context['cat_name'] = models.Category.objects.get(
                slug=self.kwargs['category'])
        except KeyError:
            pass
        ordering = self.request.GET.get('sort_by', None)
        if ordering:
            context['sort_by'] = ordering
        return context


    def paginate_queryset(self, queryset, page_size):
        """
        Process filtering
        """
        try:
            # Filter by category
            queryset = queryset.filter(category__slug=self.kwargs['category'])
        except KeyError:
            pass
        self.product_count = len(list(queryset))
        return super().paginate_queryset(queryset, page_size)


    def get_template_names(self):
        mode = self.request.GET.get('mode', 'grid')
        if mode == 'list':
            self.template_name = 'foodstore/shop-list.html'
        return self.template_name


def set_favorite_product(request, category, product_id):
    """
    Get a Product instance with id from database
    Add Product instance if its id not existed in session
    Remove Product instance if it's already existed
    """
    next_url = request.GET.__getitem__('next')
    product = models.Product.objects.get(pk=product_id)
    message = ''
    try:
        favorite_products = request.session['favorite_products']
    except KeyError:
        favorite_products = {
            'length': 0,
            'object_ids': []
        }
    queried_products = list(filter(lambda product : product == product_id, 
        favorite_products['object_ids']))
    if len(queried_products) == 0:
        favorite_products['object_ids'].append(product_id)
        message = f'You have successfully added {product} to favorite!'
    else:
        favorite_products['object_ids'].remove(queried_products[0])
        message = f'You have successfully removed {product} from favorite!'
    favorite_products['length'] = len(favorite_products['object_ids'])

    request.session['favorite_products'] = favorite_products
    
    messages.add_message(request, messages.SUCCESS, message)
    return HttpResponseRedirect(next_url)


def product_list_favorite(request):
    try:
        favorite_products = request.session['favorite_products']
        product_list = map(lambda index: models.Product.objects.get(pk=index), 
            favorite_products['object_ids'])
        product_list = list(product_list)

        def sort_list(item_list, category):
            if category == 'price':
                return sorted(item_list, key=lambda x: x.price)
            elif category == '-price':
                return sorted(item_list, key=lambda x: x.price, reverse=True)
            elif category == 'name':
                return sorted(item_list, key=lambda x: x.name)
            elif category == '-name':
                return sorted(item_list, key=lambda x: x.name, reverse=True)
            elif category == 'date_created':
                return sorted(item_list, key=lambda x: x.date_created, reverse=True)


        # Sort items
        sort_category = request.GET.get('sort_by', None)
        if sort_category:
            product_list = sort_list(product_list, sort_category)
        product_count = favorite_products['length']
    except KeyError:
        product_list = []
        product_count = 0

    # Setup paginator
    max_item_per_page = 6
    page_number = request.GET.get('page', 1)
    paginator = Paginator(product_list, max_item_per_page)
    page_obj = paginator.get_page(page_number)
    


    context = {
        'product_list': product_list,
        'product_count': product_count,
        'page_obj': page_obj
    }

    return render(request, 'foodstore/shop-grid.html', context)


def product_add_cart(request, category, product_id):
    form = AddItemToCartForm(request.POST)
    message = ''

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart = get_cart_from_session(request)
        quantity = int(cleaned_data['quantity'])

        # Add new items
        cart.add_item_to_cart(item_id=product_id,
            amount=quantity)
        product = models.Product.objects.prefetch_related(
            'review_set').get(pk=product_id)

        message = f"You have successfully added {quantity} {product} to cart"
        messages.add_message(request, messages.SUCCESS, message)
            
        # Save cart back to session
        request.session['cart'] = cart.get_serialized_data()
        return HttpResponseRedirect(reverse('products'))
    else:
        messages.add_message(request, messages.ERROR, 'There was an error occur, please try again')
        return HttpResponseRedirect(reverse('product-detail', kwargs={
            'category': category,
            'product_id': product_id
        }))
    


def product_detail(request, category, product_id):
    product = models.Product.objects.prefetch_related('review_set').select_related('category').get(pk=product_id)
    template_name = 'foodstore/shop-details.html'
    # Rendering form
    form = AddItemToCartForm()
    review_form = forms.ReviewForm()

    auth_user_review = None
    review_edit_form = None
    if request.user.is_authenticated:
        auth_user_review = product.review_set.filter(
            user=request.user)
    
        if len(auth_user_review) > 0:
            auth_user_review = auth_user_review[0]

            review_edit_form = forms.ReviewForm(data={
                'comment': auth_user_review.comment,
                'rate': auth_user_review.stars
            })
        

    # Rendering reviews for this product by page
    if request.user.is_authenticated:
        reviews = product.review_set.all().exclude(
            user=request.user)
    else:
        reviews = product.review_set.all()
    review_page_number = request.GET.get('page', 1)
    review_per_page = 1
    page_reviews_obj = Paginator(
        object_list=reviews, per_page=review_per_page)

    return render(request, template_name, {
        'product': product,
        'form': form,
        'review_form': review_form,
        'auth_user_review': auth_user_review,
        'review_edit_form': review_edit_form,
        'reviews': page_reviews_obj.page(
            number=review_page_number).object_list,
        'review_page_number': review_page_number,
        'page_reviews_obj': page_reviews_obj
    })


@login_required
def review_create(request, category, product_id):
    if request.method != 'POST':
        raise SuspiciousOperation

    review_form = forms.ReviewForm(request.POST)

    if review_form.is_valid():
        cleaned_data = review_form.cleaned_data
        product = models.Product.objects.prefetch_related('review_set').get(pk=product_id)

        # If this user reviewed this product, raise exception
        for review in product.review_set.all():
            if review.user == request.user:
                raise SuspiciousOperation

        total_review_amount_before_update = product.review_set.count()
        # Create new review
        models.Review.objects.create(
            product=product,
            user=request.user,
            comment=cleaned_data['comment'],
            stars=cleaned_data['rate']
        )
        # Update product's rating
        
        product_new_rating = (product.rating * total_review_amount_before_update + float(cleaned_data['rate'])) / (total_review_amount_before_update + 1)
        product.rating = product_new_rating
        product.save()

        return HttpResponseRedirect(reverse('product-detail',
            kwargs={
                'category': category,
                'product_id': product_id
            }))
            
    else:
        messages.add_message(request, messages.ERROR, 'Invalid input, please try again!')
        return HttpResponseRedirect(reverse('product-detail', kwargs={
            'category': category,
            'product_id': product_id
        }))


@login_required
def review_delete(request, category, product_id, review_id):
    message = ''
    review = models.Review.objects.get(pk=review_id)
    if request.user == review.user:
        product = review.product
        # Update product's rating
        total_review_amount = product.review_set.count()
        if total_review_amount == 1:
            product_new_rating = 0
        else:
            product_new_rating = (product.rating * total_review_amount - float(review.stars)) / (total_review_amount - 1)
        product.rating = product_new_rating
        product.save()
        # Dispose of the review
        review.delete()

        message = f"You have successfully deleted your review on {product}"
        messages.add_message(request, messages.SUCCESS, message)

        return HttpResponseRedirect(reverse('product-detail',
            kwargs={
                'category': category,
                'product_id': product_id
            }))
    else:
        raise PermissionDenied("You dont have permission to access this page")


@login_required
def review_update(request, category, product_id, review_id):
    if request.method != 'POST':
        raise SuspiciousOperation

    review = models.Review.objects.get(pk=review_id)
    if request.user == review.user:
        
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            old_rating = float(review.stars)
            # Update review
            cleaned_data = review_form.cleaned_data
            review = models.Review.objects.get(pk=review_id)
            review.comment = cleaned_data['comment']
            review.stars = cleaned_data['rate']
            review.save()

            # Update product's rating
            product = review.product
            total_review_amount = product.review_set.count()
            product_new_rating = (product.rating * total_review_amount + float(review.stars) - old_rating) / total_review_amount
            product.rating = product_new_rating
            product.save()

            message = f"You have successfully updated your review on {product}"
            messages.add_message(request, messages.SUCCESS, message)

            return HttpResponseRedirect(reverse('product-detail',
            kwargs={
                'category': category,
                'product_id': product_id
            }))
        else:
            messages.add_message(request, messages.ERROR, 'Invalid input, please try again!')
        return HttpResponseRedirect(reverse('product-detail', kwargs={
            'category': category,
            'product_id': product_id
        }))
    else:
        raise PermissionDenied("You dont have permission to access this page")