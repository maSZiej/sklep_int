from django.contrib import admin
from .models import Buty,Ocena


# Register your models here.
@admin.register(Buty)
class ButyAdmin(admin.ModelAdmin):
    list_display=['Nazwa','opis']
    list_filter=['Marka']

@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    list_display=['przedmiot','komentarz']