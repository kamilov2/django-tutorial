from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.

GENDERS = (
    ("male","Male"),
    ("female","Female"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="users_images/", blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100,choices=GENDERS, blank=True)
    country = CountryField()
    
    
    def __str__(self):
        return self.user.username
    