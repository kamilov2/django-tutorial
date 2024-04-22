import datetime
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.title




class Author(models.Model):
    name = models.CharField(max_length=150)
    actor = models.BooleanField(default=False)
    director = models.BooleanField(default=False)
    producer  = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

QUAITY = (
    ('ts',"TS"),
    ('bdrip',"BDRIP"),
    ('hdrip',"HDRIP")
)

class Movie(models.Model):
    poster = models.ImageField(upload_to='posters/%Y/%B', blank=True)
    name = models.CharField(max_length=150)
    origin_name = models.CharField(max_length=150, blank=True)
    year = models.PositiveSmallIntegerField(default=0)
    genres = models.ManyToManyField(Genre)
    quality = models.CharField(choices=QUAITY, max_length=150, blank=True)
    author = models.ManyToManyField(Author, related_name="movies")
    duration = models.CharField(max_length=150, blank=True)
    short_description = models.TextField(blank=True)
    sd_file_url = models.URLField(blank=True)
    hd_file_url = models.URLField(blank=True)

    rating = models.FloatField(default=0)
    imdb_rating = models.FloatField(default=0)
    kp_rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=150, default="Guest")
    text = models.TextField()

    def __str__(self) -> str:
        return self.name


