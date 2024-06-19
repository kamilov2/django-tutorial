from django.db import models

# Create your models here.
class Leaguage(models.Model):
    name = models.CharField("Liga nomi", max_length=250)
    logo = models.ImageField(upload_to="leaguages/", blank=True)
    country = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField("Klub nomi", max_length=250)
    logo = models.ImageField(upload_to="clubs/", blank=True)
    leaguage = models.ForeignKey(Leaguage, on_delete=models.CASCADE, related_name="clubs")
    country = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
POS = (
    ("gk","Darvozabon"),
    ("df","Himoyachi"),
    ("mdf","Yarim Himoyachi"),
    ("fw","Hujumkor himoyachi"),
    ("st","Hujumchi"),
)

class Player(models.Model):
    name = models.CharField("Player nomi", max_length=250)
    image = models.ImageField(upload_to="players/", blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="players")
    country = models.CharField(max_length=250)
    date_of_birth = models.DateTimeField()
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    position = models.CharField(max_length=50, choices=POS)
    
    def __str__(self):
        return self.name