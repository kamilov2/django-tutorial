from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import TemplateView # TemplateView - oddiy htmlni response sifatida qaytarish
from django.views.generic import ListView, DetailView
from .models import Club,Leaguage,Player
from blog.models import Post

# Create your views here.

class HomePageView(ListView):
    model = Leaguage
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        context["players"] = Player.objects.all()
        context["posts"] = Post.objects.all()
        
        
        return context
    
class LeaguageDetailView(DetailView) :
    model = Leaguage
    template_name = 'leaguage.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.filter(leaguage=self.object)
        return context
      
class ClubDetailView(DetailView) :
    model = Club
    template_name = 'club.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = Player.objects.filter(club=self.object)
        return context    
    
class PlayerDetailView(DetailView) :
    model = Player
    template_name = 'player.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.filter(player=self.object)  
        return context     
    
class CantactPageView(TemplateView):
    template_name = "contact.html"
    
    
    
def filter_by_position(request):
    if request.method == 'POST':
        pos = request.POST.get("position")
        players = Player.objects.filter(position=pos)
        data = {
            "players":players
        }
    return render(request,'result.html', context=data)

def filter_by_age(request):
    if request.method  == "POST":
        min_age_range = request.POST.get("min_age")
        max_age_range = request.POST.get("max_age")
        players = Player.objects.filter(date_of_birth__range=[min_age_range,max_age_range])
        data = {
            "players":players
        }
    return render(request, 'result.html', context=data)

def filter_by_height(request):
    if request.method  == "POST":
        min_height_range = request.POST.get("min_height")
        max_height_range = request.POST.get("max_height")
        players = Player.objects.filter(height__range=[min_height_range,max_height_range])
        data = {
            "players":players
        }
    return render(request, 'result.html', context=data)

def filter_by_country(request):
    if request.method == "POST":
        country = request.POST.get("country")
        players  = Player.objects.filter(country=country)
        data = {
           "players":players
        }
    return render(request,'result.html', context=data)