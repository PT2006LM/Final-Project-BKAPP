from django.shortcuts import render


def homepage(request):
    return render(request, 'base_templates/homepage.html')

def browser(request):
    return render(request, 'base_templates/browserpage.html')