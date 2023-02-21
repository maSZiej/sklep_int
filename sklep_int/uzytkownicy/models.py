from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Buty(models.Model):
    Nazwa = models.CharField(max_length=255)
    Marka = models.TextField(default='Nike')
    Wyglad = models.ImageField(upload_to='static')
    opis = models.TextField()

    class Rozmiar(models.IntegerChoices):
        male1 = 38
        male2 = 39
        srednie1 = 40 
        srednie2 = 41
        duze1 = 42 
        duze2 = 43
    wybor = models.IntegerField(choices=Rozmiar.choices,default=Rozmiar.srednie1)

    def __str__(self):
        return self.Nazwa

    

class Ocena(models.Model):
    przedmiot = models.ForeignKey(Buty, on_delete=models.CASCADE)
    komentarz=models.TextField()
