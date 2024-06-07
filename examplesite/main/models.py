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
    course = models.ForeignKey( # birga ko'p ulash
        to=Course, 
        on_delete=models.PROTECT, # agar kurs o'chib ketsa guruhlar qoladi
        related_name="groups", # murojaat qilish uchun nom 
        null=True)
    name = models.CharField(verbose_name="Guruh nomi",max_length=250)
    teach_days = models.CharField(max_length=250, choices=DAYS)
    price = models.PositiveBigIntegerField(default=0)
    room = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    group = models.ForeignKey( # birga ko'p ulash
        to=Group, 
        on_delete=models.PROTECT, # agar kurs o'chib ketsa guruhlar qoladi
        related_name="students", # murojaat qilish uchun nom 
        null=True)
    first_name = models.CharField("Ismi", max_length=250)
    last_name = models.CharField("Familya", max_length=250)
    phone = models.CharField("Telefon", max_length=250)
    address = models.CharField("Manzil", max_length=250)

    def __str__(self):
        return f"{self.first_name}"