from django.shortcuts import render,redirect
from django.views.generic import View
from main.models import Product
from .models import Cart,CartProducts

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create() # yangi cart object hosil qilish
        request.session['user_cart_id'] = cart.id
    return cart


# Create your views here.
class CartView(View):
    
    def get(self, request):
        cart = cart_init(request)
        return render(request, "cart.html",{"cart":cart})

def add_product(request, product_id):
    cart = cart_init(request)
    cart.add(product_id)
    return redirect("/cart/")

def cart_product_update(request,action,product_id,item_id):
    cart = cart_init(request)
    item = CartProducts.objects.get(id=item_id)
    if item.quantity == 1 and action == "minus":
        return redirect("/cart/")
    else:
        cart.cart_product_update(action,product_id,item_id)
    return redirect("/cart/")