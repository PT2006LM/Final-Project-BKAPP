from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html', {
        'heading_menu': 'home'
    })

def contact(request):
    return render(request, 'contact.html')