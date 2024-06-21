from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.
from .models import Leaguage,Club,Player


class HomePageView(ListView):
    model = Player
    template_name = "players.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leagueages"] = Leaguage.objects.all()
        context["clubs"] = Club.objects.all()
        context["text"] = """<i>Python</i> is better !"""
        context["numbers"] = list(range(1,16))
        
        return context
    