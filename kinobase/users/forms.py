from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SimpleUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","first_name","password1","password2"]
        widgets = {
            "username":forms.TextInput(attrs={"class":"input w100","required":""}),
            "first_name":forms.TextInput(attrs={"class":"input w100","required":""}),
            "password1":forms.PasswordInput(attrs={"class":"input w100"}),
            "password2":forms.PasswordInput(attrs={"class":"input w100"})
        }


