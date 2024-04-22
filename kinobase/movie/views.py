from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import *


class HomePageView(ListView):
    model = Movie
    template_name = "kinobase.org/index.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "kinobase.org/film.html"