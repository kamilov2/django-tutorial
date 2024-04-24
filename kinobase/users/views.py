from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.contrib.auth.models import User
from .models import Profile


# Create your views here.
def my_logout(request):
    logout(request)
    return redirect("/users/login/")


def my_register(request):
    if request.method == "POST":
        username = request.POST.get("email").split("@")[0]
        name = request.POST.get("name")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password_confirmation")

        if all([username,name,pass1,pass2]):
            if pass1 == pass2:
                u = User.objects.create(username=username,first_name=name,password=pass2)
                Profile.objects.create(user=u)

                print("OK")
                return redirect("/users/login/")
            else:
                print("password didnt match")


        print(username,name,pass1, pass2)
    return render(request, "kinobase.org/auth/registration.html")