from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="kinobase.org/auth/login.html"
    ), name="login"),

    path("logout/", views.my_logout, name="logout"),

    path("registration/", views.my_register, name="register")
]
