from django import template

register = template.Library()

# source: https://stackoverflow.com/questions/6453652/how-to-add-the-current-query-string-to-an-url-in-a-django-template
@register.simple_tag
def add_query_params(request, **kwargs):
    """
    Takes a request and generates URL with given kwargs as query parameters
    e.g.
    1. {% add_query_params request key=value %} with request.path=='/ask/'
        => '/ask/?key=value'
    2. {% add_query_params request page=2 %} with request.path=='/ask/?key=value'
        => '/ask/?key=value&page=2'
    3. {% add_query_params request page=5 %} with request.path=='/ask/?page=2'
        => '/ask/?page=5'
    """
    updated = request.GET.copy()
    for key, value in kwargs.items():
        updated[key] = value

    return request.build_absolute_uri('?'+updated.urlencode())