from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Profile


# Create your views here.
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        # print(email, first_name, last_name, password, password_confirmation)

        if all([email, first_name, last_name, password, password_confirmation]):
            if password == password_confirmation:
                u = User.objects.create_user(username=email,email=email, first_name=first_name, last_name=last_name, password=password)
                authenticate(request, email=email, password=password)
                Profile.objects.create(user=u)
                login(request, u)
                return redirect("/")
    return render(request, 'auth/registration.html')