from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.MovieListView.as_view(), name="movie_list"),
    path("movie/<slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
]