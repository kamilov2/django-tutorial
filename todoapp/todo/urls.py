from django.urls import path 
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    
    path("add/", views.AddTodoView.as_view(), name="add"),
    
    path('update/<int:pk>', views.UpdateToDo.as_view(),name='update')
    
]
