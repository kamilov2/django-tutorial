from django.urls import path
from . import views
app_name = "movie"



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("film/<slug>", views.MovieDetailView.as_view(), name='detail'),

    path("film/add-to-favorite/<int:movie_id>", views.add_to_favorite, name="add_to_favorite"),

    path("favorites/", views.favorite_list, name="favorites"),
    path("history/", views.history_list, name="history"),
]
