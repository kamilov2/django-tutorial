from django.shortcuts import render
from django.views.generic import View
from main.models import Product
from .models import Cart

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
        request.session.modified = True
        # request.session["my_name"] = "Rustam"
        # print(request.session["my_name"]) # Rustam
        return render(request, "cart.html")

def add_product(request, product_id):
    cart = cart_init(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    return render(request, "cart.html")