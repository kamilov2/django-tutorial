from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users/",blank=True)
    favourites = models.ManyToManyField(Movie, related_name="user_favorites")
    views = models.ManyToManyField(Movie, related_name="user_views")

    def __str__(self):
        return self.user.username