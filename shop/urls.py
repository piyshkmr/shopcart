from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('contact', views.contact, name="Contact"),
    path('product/<int:id>', views.productDetail, name="Product"),
    path('checkout', views.checkout, name="checkout"),
    # path('search', views.search, name="Search"),
    path('orders', views.orders, name="Orders"),
    path('cart', views.cart, name="Cart"),
    path('addToCart', views.addToCart, name="addToCart"),
    path('removeFromCart', views.removeFromCart, name="removeFromCart"),
]
