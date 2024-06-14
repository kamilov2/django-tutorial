from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.HomePageView.as_view(),name="home"),
    
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="detail")
]
