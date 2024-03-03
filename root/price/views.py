from django.shortcuts import render

def index(request):
    return render(request, 'price/index.html', {
        'title': 'Прайс',
        'page': 'index',
        'app': 'price',
    })


