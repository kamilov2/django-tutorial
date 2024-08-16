from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
    
class Genre(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    origin_title = models.CharField(max_length=250, blank=True)
    cover = models.ImageField(upload_to="movie/covers/", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="movies")
    genre = models.ManyToManyField(Genre, related_name="mouvies")
    country = CountryField(multiple=True,blank=True)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(default=0)
    rating_count = models.PositiveSmallIntegerField(default=0)
    kp_rating = models.FloatField(default=0)
    imdb_rating = models.FloatField(default=0)
    quality = models.CharField(max_length=150, choices=[('ts', 'TS'), ('hdrip', 'Hdrip'), ('bdrip', 'Bdrip'),])
    duration = models.CharField(max_length=150,blank=True)
    file_url = models.URLField(blank=True)
    related_films = models.ManyToManyField("self", blank=True)
    
    def __str__(self):
        return str(self.title)
    
    def get_avg_rating(self):
        ratings = self.ratings.all()
        if ratings:
            value = sum([item.value for item in ratings]) / len(ratings)
            if value:
                return value
            else:
                return 0
        else:
            return 0
    

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    value = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_ratings")


    def __str__(self):
        return f"{self.user.username} - {self.movie.title} = {self.value}"
    
    
class Author(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")
    author = models.ManyToManyField(Author)
    
    actor = models.BooleanField(default=False)
    director = models.BooleanField(default=False)
    producer = models.BooleanField(default=False)
    writer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.author.name or "empty"


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username or "empty"