from foodstore import models

def category_processor(request):
    category_list = models.Category.objects.all()
    category_count = len(category_list)
    return {
        'category_list': category_list,
        'category_count': category_count
    }

def product_processor(request):
    product_list = models.Product.objects.all()
    product_count = len(product_list)
    return {
        'product_list': product_list,
        'product_count': product_count
    }