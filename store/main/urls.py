from django.urls import path 
from . import  views

app_name = "main"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home" ),
    path("detail/<slug:slug>", views.ProductDetailView.as_view(), name="detail" ),
]
