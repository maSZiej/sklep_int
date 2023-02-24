from django.contrib import admin
from django.utils.html import format_html
from .models import Buty,Ocena,Marki


class oclin(admin.TabularInline):
    model = Ocena

# Register your models here.
@admin.register(Buty)
class ButyAdmin(admin.ModelAdmin):
    list_display=['Nazwa','opis','cena','wyglad']
    list_filter=['Marka']
    search_fields=['Nazwa']
    inlines = [
        oclin
    ]

    def obr(self,obj):
        return format_html(f'<image hight=10px width=10px src={obj}>')    


@admin.register(Ocena)
class OcenaAdmin(admin.ModelAdmin):
    list_display=['przedmiot','komentarz']

    def __str__(self):
        return ''
    
@admin.register(Marki)
class MarkiAdmin(admin.ModelAdmin):
    list_display=['nazwa','Logo']