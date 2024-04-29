from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import *

from .utils import get_movie_filter_years, get_country_list


class HomePageView(ListView):
    model = Movie
    template_name = "kinobase.org/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
  
        context["genres"] = Genre.objects.all()
        context["years"] = get_movie_filter_years()
        context["countries"] = get_country_list()
        return context
    


class MovieDetailView(DetailView):
    model = Movie
    template_name = "kinobase.org/film.html"


    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            self.request.user.profile.views.add(self.object)
        context = super().get_context_data(**kwargs)
        return context
    



def add_to_favorite(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    if movie not in request.user.profile.favourites.all():
        request.user.profile.favourites.add(movie)
        messages.success(request,"Movie added to favourites !")
    else:
        request.user.profile.favourites.remove(movie)
        messages.success(request,"Movie deleted from favourites !")
    # request.user.profile.user_favorites.add(movie)
    return redirect("/")


def favorite_list(request):
    movies = request.user.profile.favourites.all()
    return render(request, "kinobase.org/auth/favorites.html", context={"object_list":movies})


def history_list(request):
    movies = request.user.profile.views.all()
    return render(request, "kinobase.org/auth/history.html", context={"object_list":movies})




def movie_filter(request,filter_by_what,filter_data):
    if filter_by_what == "genre":
        filtering_genre = Genre.objects.get(title=filter_data)
        object_list = Movie.objects.filter(genres=filtering_genre)
        return render(request,"kinobase.org/films.html", context={"object_list":object_list})
    
    if filter_by_what == "year":
        object_list = Movie.objects.filter(year=int(filter_data))
        return render(request,"kinobase.org/films.html", context={"object_list":object_list})
    
    if filter_by_what == "country":
        object_list = []
        for movie in Movie.objects.all():
            for data in movie.country:
                if filter_data == data.name:
                    object_list.append(movie)
        return render(request,"kinobase.org/films.html", context={"object_list":object_list})
    
    if filter_by_what == "quality":
        object_list = Movie.objects.filter(quality=filter_data.lower())
        return render(request,"kinobase.org/films.html", context={"object_list":object_list})