from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
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
    
    