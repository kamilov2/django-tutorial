from django.urls import path,reverse_lazy
from django.contrib.auth.views import *

from .import views

app_name = 'users'

urlpatterns = [
    path("login/", LoginView.as_view(template_name="auth/login.html"), name='login'),
    path("logout/", views.logout_view, name='logout'),
    
    path("register/",views.register, name='register'),
    path("password_change/",PasswordChangeView.as_view(
        template_name="auth/password_change_form.html",
        success_url="/"
        ), name='password_change'),
    
    path("password-reset/", PasswordResetView.as_view(
        template_name="auth/password_reset_form.html",
        email_template_name="auth/password_reset_email.html",
        html_email_template_name="auth/password_reset_email.html",
        success_url=reverse_lazy("users:password_reset_done")), name='password_reset'),
    
    path("password-reset/done/", PasswordResetDoneView.as_view(
        template_name="auth/password_reset_done.html"), name='password_reset_done'),
    
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        template_name="auth/password_reset_confirm.html",
        success_url=reverse_lazy("users:password_reset_complete")), name='password_reset_confirm'),
    
    path("password-reset/complete/", PasswordResetCompleteView.as_view(
        template_name="auth/password_reset_complete.html"), name='password_reset_complete'),
    
    path("profile/<pk>", views.ProfileDetailView.as_view(), name='profile'),
    
    path("profile/edit/<pk>", views.ProfileUpdateView.as_view(), name='profile_update')
]
