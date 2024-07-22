from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import Product,Category
# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = "index.html"
    
    def get_queryset(self):
        return Product.objects.filter(avilable=True)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Product.objects.filter(subcategory__category__slug="chexollar") 
        context["headphones"] = Product.objects.filter(subcategory__category__slug="quloqchinlar") 
        print(context["cases"])
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"


class WishListView(ListView):
    model = Product
    template_name = "liked_product.html"
    
    def get_queryset(self):
        try:
            wishlist = self.request.session["wishlist"]
        except:
            wishlist = self.request.session["wishlist"] = []
        return Product.objects.filter(id__in=wishlist)

def add_wishlist(request,product_id):
    product = Product.objects.get(id=product_id)
    request.session.modified = True
    try:
        wishlist = request.session["wishlist"]
    except:
        wishlist = request.session["wishlist"] = []
    if product.id in wishlist:
        wishlist.remove(product.id)
        messages.info(request,"Tovar wishlistdan o'chirildi !")
    else:
        wishlist.append(product.id)
        messages.info(request,"Tovar wishlistga qo'shildi !")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))