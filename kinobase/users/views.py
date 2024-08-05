from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

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
                if len(email.split("@")[0]) > 6:
                    email = email.split("@")[0]
                u = User.objects.create_user(username=email,email=email, first_name=first_name, last_name=last_name, password=password)
                authenticate(request, email=email, password=password)
                Profile.objects.create(user=u)
                login(request, u)
                return redirect("/")
    return render(request, 'auth/registration.html')

class ProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "auth/profile.html"
    slug_field = "username"
    slug_url_kwarg = 'username'
    
    
def profile_update(request):
    image = request.FILES.get('avatar_file')
    print(image)
    email = request.POST.get('email')
    first_name = request.POST.get('name')
    password = request.POST.get('password')
    password_confirmation = request.POST.get('password_confirmation')
    # print(email,image, first_name, password, password_confirmation)
    profile = request.user.profile
    if image:
        profile.image = image
        profile.save()
        messages.success(request,"Rasm yangilandi !")
    if email:
        request.user.email = email
        request.user.save()
        messages.success(request,"Email yangilandi !")
    if first_name:
        request.user.first_name = first_name
        request.user.save()
        messages.success(request,"Ism yangilandi !")
    if password and password_confirmation:
        if password == password_confirmation:
            request.user.set_password(password)
            request.user.save()
            messages.success(request,"Parol yangilandi !")
            
        
    
    return redirect("/")
