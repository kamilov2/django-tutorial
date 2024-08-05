from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = "users"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
        template_name="auth/registration.html"), name="login"),
    path("register/", views.register, name="register"),
    path("profile/<str:username>", views.ProfileView.as_view(), name="profile"),
    path("profile_update/", views.profile_update, name="profile_update")
]