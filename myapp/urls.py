from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"),

    path("login/", views.login, name="login"),
   
    path('myorder', views.myorder, name="myorder"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('feedback', views.feedback, name='feedback'),

    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]