from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.MovieListView.as_view(), name="movie_list"),
    path("movie/detail/<slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("comment/delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    path("movie/set_rating/<int:rating_value>/<int:movie_id>/", views.set_rating, name="set_rating"),
    path("movie/add/favorite/<int:movie_id>", views.add_favorite, name="add_to_favorite"),
    path("movie/add/favorites/", views.favourites_page, name="favourites_page"),
    path("category/<slug:slug>", views.category, name="category"),
    path("genre_filter/", views.genre_filter, name="filter_genre"),
    path("sort/<str:key>", views.movie_sort, name="sort"),
    path("search/", views.search, name="search"),
]
