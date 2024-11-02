from django.shortcuts import render, HttpResponse

def home(request):
    context = {}
    return render(request, 'home.html', context)



def login(request):
    context = {}
    return render(request, 'login.html', context)

def aboutus(request):
    context = {}
    return render(request, 'aboutus.html', context)

def myorder(request):
    context = {}
    return render(request, 'myorder.html', context)

def feedback(request):
    context = {}
    return render(request, 'feedback.html', context)



def products(request):
    context = {}
    return render(request, 'products.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)