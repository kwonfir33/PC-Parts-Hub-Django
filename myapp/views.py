from django.shortcuts import render, HttpResponse
from .models import *
# handles request/response logic view > model > template

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
    # fetch every record from Product Model DB then send to template
    products = Product.objects.all() 
    context = {'products':products}
    return render(request, 'products.html', context)

def cart(request):
    if request.user.is_authenticated:
        #user logged in (saved items rendered)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #user in guest mode (empties the cart)
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        #user logged in (saved items rendered)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #user not logged in / guest(set all values to 0) 
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)