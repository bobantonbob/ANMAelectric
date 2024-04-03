from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home',
    })


def about(request):
    return render(request, 'home/about.html', {
        'title': 'Про ANMA',
        'page': 'about',
        'app': 'home',
    })


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html', {
        'title': 'Політика конфіденційності',
        'page': 'privacy_policy',
        'app': 'home',
    })

def warranty(request):
    return render(request, 'home/warranty.html', {
        'title': 'Гарантія ',
        'page': 'warranty',
        'app': 'home',
    })


def orders(request):
    return render(request, 'home/orders.html', {
        'title': 'Заявка ',
        'page': 'orders',
        'app': 'home',
    })

def lightning(request):
    return render(request, 'home/lightning.html', {
        'title': 'Блискавкозахист ',
        'page': 'lightning',
        'app': 'home',
    })

def grounding(request):
    return render(request, 'home/grounding.html', {
        'title': 'Заземлення ',
        'page': 'grounding',
        'app': 'home',
    })