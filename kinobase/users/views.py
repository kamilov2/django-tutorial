from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login

from django.contrib.auth.models import User
from .models import Profile
from .forms import SimpleUserCreationForm

# Create your views here.
def my_logout(request):
    logout(request)
    return redirect("/users/login/")


def my_register(request):
    form = SimpleUserCreationForm()
    if request.method == "POST":
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            Profile.objects.create(user=u)
            authenticate(request,username=u.username,password=u.password)
            login(request, u)
            return redirect("/")
        else:
            return redirect("/users/register/")
        


    return render(request, "kinobase.org/auth/registration.html", context={"form":form})