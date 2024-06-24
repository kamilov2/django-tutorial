from django.urls import path 
from . import views

app_name = "players"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="player_home"),
    path("add/leaguage", views.add_leaguage, name="add_leaguage")
]
