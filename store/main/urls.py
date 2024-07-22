from django.urls import path 
from . import  views

app_name = "main"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home" ),
    path("detail/<slug:slug>", views.ProductDetailView.as_view(), name="detail" ),
    path("wishlist/", views.WishListView.as_view(), name="wishlist" ),
    path("wishlist/add/<int:product_id>", views.add_wishlist, name="add_wishlist" ),
]
