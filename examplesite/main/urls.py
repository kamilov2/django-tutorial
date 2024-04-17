from django.urls import path
from django.http import HttpResponse
from . import views

app_name = "main"

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home" ),
    path('leaguage/<pk>', views.LeaguageDetailView.as_view(),name='leaguage_detail'),
    path('club/<pk>', views.ClubDetailView.as_view(),name='club_detail'),
    path('player/<pk>', views.PlayerDetailView.as_view(),name='player_detail'),
    #FILTER
    path('filter/position', views.filter_by_position, name='filter_by_position' ),
    path('filter/age', views.filter_by_age, name='filter_by_age' ),
    path('filter/height', views.filter_by_height, name='filter_by_height' ),
    path('filter/country', views.filter_by_country, name='filter_by_country' )
]


# views - asosiy logika 
# controller method  - def 
# controller class - class 