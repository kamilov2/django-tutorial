from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.
from .models import Leaguage,Club,Player

from .forms import AddLeaguageForm


class HomePageView(ListView):
    model = Player
    template_name = "players.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leagueages"] = Leaguage.objects.all()
        context["clubs"] = Club.objects.all()
        context["text"] = """<i>Python</i> is better !"""
        context["numbers"] = list(range(1,16))
        context["form"] = AddLeaguageForm()
        return context

def add_leaguage(request):
    # print(request.POST)
    # print(request.FILES)
    name = request.POST.get("name")
    country = request.POST.get("country")
    logo = request.FILES.get("logo")
    print(name)
    print(country)
    print(logo)
    Leaguage.objects.create(
        name=name,
        logo=logo,
        country=country
    )
    print("Success")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))