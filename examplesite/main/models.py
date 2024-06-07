from django.db import models
# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name="Kurs nomi",max_length=250)
    duration = models.CharField("Davomiyligi", max_length=250)
    
    def __str__(self):
        return f"{self.name}"

DAYS = (
    ("dchj","Du-Chor-Ju"),
    ("spsh","Se-Pa-Sha"),
)
class Group(models.Model):
    name = models.CharField(verbose_name="Guruh nomi",max_length=250)
    teach_days = models.CharField(max_length=250, choices=DAYS)
    price = models.PositiveBigIntegerField(default=0)
    room = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}"
