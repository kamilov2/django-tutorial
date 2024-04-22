from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import *


class HomePageView(ListView):
    model = Movie
    template_name = "kinobase.org/index.html"