import datetime
from django.db import models

# Create your models here.
class Leaguage(models.Model):
    name = models.CharField("Liga yoki Chempionat nomi",max_length=250)
    logo = models.ImageField(upload_to="leaguage/logos/")
    country = models.CharField("Davlat", max_length=100)
    
    def __str__(self):
        return str(self.name)

class Club(models.Model):
    name = models.CharField("Klub nomi",max_length=250)
    logo = models.ImageField(upload_to="club/logos/")
    country = models.CharField("Davlat", max_length=100)
    coach = models.CharField("Trener", max_length=100)
    leaguage = models.ForeignKey(Leaguage,on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.name)

POS = (
    ('gk','Darvozabon'),
    ('df','Himoyachi'),
    ('md','Yarim himoyachi'),
    ('fw','Hujumkor himoyachi'),
    ('st','Hujumchi'),
)

class Player(models.Model):
    name = models.CharField("Ism-Sharif",max_length=250)
    image = models.ImageField(upload_to="players/images/")
    date_of_birth = models.DateField("Tugilgan sanasi")
    country = models.CharField("Davlat", max_length=100)
    club = models.ForeignKey(Club,on_delete=models.PROTECT)
    position = models.CharField(max_length=100,choices=POS)
    transfer_summa = models.PositiveIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)
    
    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.date_of_birth.year
        return age
    
    def __str__(self):
        return str(self.name)
    