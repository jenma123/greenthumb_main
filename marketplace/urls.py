from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace, name='marketplace'),
    path('cart/', views.cart, name='cart'),
    path('<slug:vendor_slug>/', views.vendor_detail, name='vendor_detail'),
    path('add_to_cart/<int:plant_id>/', views.add_to_cart, name='add_to_cart'),
    # DECREASE CART
    path('decrease_cart/<int:plant_id>/', views.decrease_cart, name='decrease_cart'),
    # DELETE CART ITEM
    path('delete_cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),


    
]