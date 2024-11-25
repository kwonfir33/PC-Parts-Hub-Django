from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer, Order, OrderItem, Product
from django.http import JsonResponse
import json
from django.contrib.auth import logout
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:  # Only create the customer if the user was newly created
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    try:
        instance.customer.save()  # Save the associated customer object
    except Customer.DoesNotExist:
        pass  # No action if customer does not exist

# Home view
def home(request):
    return render(request, 'home.html')

# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Stay on login page with error message
    
    return render(request, 'login.html')

# Registration view
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact_no = request.POST['contact_no']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Create the user profile and save additional info
        profile = Profile(user=user, contact_no=contact_no)
        profile.save()
        
        auth_login(request, user)
        return redirect('home')  # Redirect to the homepage after successful registration
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)  # Logs out the current user
    return redirect('home')  # Redirects to the home page after logging out

# About us view
def aboutus(request):
    context = {}
    return render(request, 'aboutus.html', context)

# My orders view
def myorder(request):
    context = {}
    return render(request, 'myorder.html', context)

# Feedback view
def feedback(request):
    context = {}
    return render(request, 'feedback.html', context)

# Products view (this page lists products and cart items)
def products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'products.html', context)

# Cart view (this page shows the user's cart)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)

# Checkout view (this page is where users review and confirm their orders)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)

# Update cart items (this will handle add/remove items from the cart)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

