from django.urls import path 
from . import views 

app_name = "main"

urlpatterns = [
    path("",views.home_page, name="home"),
    path("course/<int:course_id>", views.course_detail, name="course_detail")
]
