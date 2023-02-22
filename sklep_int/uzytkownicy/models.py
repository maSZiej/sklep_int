from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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

    

class Ocena(models.Model):
    przedmiot = models.ForeignKey(Buty, on_delete=models.CASCADE)
    komentarz=models.TextField()
#    data = models.SlugField(max_length=250,unique_for_date='opublikowano')

    def __str__(self):
        return ''    