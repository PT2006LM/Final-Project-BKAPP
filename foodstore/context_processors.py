from foodstore import models

def category_processor(request):
    category_list = models.Category.objects.all()
    return {
        'category_list': category_list
    }