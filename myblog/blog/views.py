from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView

from .models import Category,Tag,Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "object_list"
    
    def get_queryset(self): # SELECT * FROM Post
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =  Category.objects.all()
        return context
    

class PostDetailView(DetailView):
    model = Post # Post.objects.get()
    template_name = "detail.html"
    
    
    def get_queryset(self): # SELECT * FROM Post WHERE slug=slug
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =  Category.objects.all()
        return context