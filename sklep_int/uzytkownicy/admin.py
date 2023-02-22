from django.contrib import admin
from django.utils.html import format_html
from .models import Buty,Ocena


class oclin(admin.TabularInline):
    model = Ocena

# Register your models here.
@admin.register(Buty)
class ButyAdmin(admin.ModelAdmin):
    list_display=['Nazwa','opis','obr']
    list_filter=['Marka']
    search_fields=['Nazwa']
    inlines = [
        oclin
    ]

    def obr(self,obj):
        return format_html(f'<image src={obj}>')

@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    list_display=['przedmiot','komentarz']

    def __str__(self):
        return ''