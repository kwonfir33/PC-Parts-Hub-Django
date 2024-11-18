from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_user, name="logout"),  # For logging out
    path('myorder', views.myorder, name="myorder"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('feedback', views.feedback, name='feedback'),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/',views.updateItem, name="update_item"),
]
