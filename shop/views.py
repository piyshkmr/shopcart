
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Cart, Contact, Order, Product
import json


# Create your views here.


def index(request):
    cartItemCount = 0
    products = Product.objects.all()

    categories = [
        {"name": "Fashion", "products": products.filter(category="Fashion")},
        {"name": "Electronics", "products": products.filter(
            category="Electronics")},
        {"name": "Education", "products": products.filter(
            category="Education")},
        {"name": "Essentials", "products": products.filter(
            category="Essentials")},
    ]

    for item in Cart.objects.all():
        cartItemCount += item.quantity

    return render(request, "shop/index.html", {"categories": categories, "products": products, "cartItemCount": cartItemCount})


def contact(request):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    message = request.POST.get("message", "")
    show = False

    if(name != ""):
        Contact(name=name, email=email, phone=phone, message=message).save()
        show = True

    return render(request, "shop/contact.html", {"show": show})


def productDetail(request, id):

    cartItemCount = 0

    productExistInCart = False
    product = Product.objects.filter(id=id).first()
    cartItem = Cart.objects.filter(id=id).first()

    if cartItem:
        productExistInCart = True

    for item in Cart.objects.all():
        cartItemCount += item.quantity

    return render(request, "shop/product.html", {"product": product, "productExistInCart": productExistInCart, "cartItemCount": cartItemCount})


def orders(request):
    cartItemCount = 0

    for item in Cart.objects.all():
        cartItemCount += item.quantity

    orders = Order.objects.all()

    return render(request, "shop/orders.html", {"cartItemCount": cartItemCount, "orders": orders})


def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        state = request.POST.get("state")
        city = request.POST.get("city")
        phone = request.POST.get("phone")
        items = request.POST.get("items")
        totalAmount = request.POST.get("totalAmount")

    Order(name=name, email=email, phone=phone, address=address,
          state=state, city=city, items=json.dumps(items), totalAmount=totalAmount).save()

    Cart.objects.all().delete()

    return render(request, "shop/cart.html", {"cartItemCount": 0, "show": True})


def cart(request):
    total = 0
    cartItemCount = 0
    deliveryCharge = 45
    cart = Cart.objects.all()

    for item in cart:
        cartItemCount += item.quantity
        total += item.price*item.quantity

    return render(request, "shop/cart.html", {"cart": cart, "total": total, "deliveryCharge": deliveryCharge, "totalAmount": total+deliveryCharge, "cartItemCount": cartItemCount})


def addToCart(request):
    name = request.GET.get("name")
    price = int(request.GET.get("price"))
    image = request.GET.get("image")
    id = request.GET.get("id")
    redirectToCart = request.GET.get("redirect")

    cartItem = Cart.objects.filter(id=id).first()

    if(cartItem):
        qnt = cartItem.quantity + 1
        Cart.objects.filter(id=id).update(quantity=qnt)

    else:
        Cart(name=name, price=price, image=image, id=id).save()

    if(redirectToCart == "yes"):
        return redirect("/shop/cart")

    else:
        return redirect("/shop/product/"+id)


def removeFromCart(request):
    id = request.GET.get("id")
    delete = request.GET.get("delete")

    if(delete == "yes"):
        Cart.objects.filter(id=id).delete()
        return redirect("/shop/cart")

    cartItem = Cart.objects.filter(id=id).first()

    if(cartItem):
        qnt = max(cartItem.quantity - 1, 0)
        Cart.objects.filter(id=id).update(quantity=qnt)

    return redirect("/shop/cart")
