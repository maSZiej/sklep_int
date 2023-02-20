from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Przedmiot(models.Model):
    Nazwa = models.CharField(max_length=255)
    opis = models.TextField()

    class Buty(models.IntegerChoices):
        male1 = 38
        male2 = 39
        srednie1 = 40
        srednie2 = 41
        duze1 = 42
        duze2 = 43
    wybor = models.IntegerField(choices=Buty.choices)

class Ocena(models.Model):
    przedmiot = models.ForeignKey(Przedmiot, on_delete=models.CASCADE)
    komentarz=models.TextField()
    