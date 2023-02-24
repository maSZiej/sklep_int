from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


# Create your models here.
class Buty(models.Model):
    Nazwa = models.CharField(max_length=255)
    Marka = models.TextField(default='Nike')
    Wyglad = models.ImageField(upload_to='static')
    opis = models.TextField()

    class Rozmiar(models.IntegerChoices):
        male_38 = 38
        male_39 = 39
        srednie_40 = 40 
        srednie_41 = 41
        duze_42 = 42 
        duze_43 = 43
    rozmiar = models.IntegerField(choices=Rozmiar.choices,default=Rozmiar.srednie_40)

    def __str__(self):
        return self.Nazwa

    def wyglad(self): #new
        return mark_safe(f'<img src = "{self.Wyglad.url}" width = "20" height="20" />')
        


class Ocena(models.Model):
    przedmiot = models.ForeignKey(Buty, on_delete=models.CASCADE)
    komentarz=models.TextField()
#    data = models.SlugField(max_length=250,unique_for_date='opublikowano')

    def __str__(self):
        return ''    
    

class Marki(models.Model):
    nazwa = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static')

    def Logo(self): #new
        return mark_safe(f'<img src = "{self.logo.url}" width = "20" height="20" />')