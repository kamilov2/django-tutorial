from django.urls import path
from . import views
app_name = "movie"



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path("film/<slug>", views.MovieDetailView.as_view(), name='detail')
]
