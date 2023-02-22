from .models import Buty,Ocena
from rest_framework import serializers

class ButySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Buty
        fields = ['Nazwa','Marka','Wyglad','opis']

#class OcenaSerializer(serializers.HyperlinkedModelSerializer):
    
  #  class Meta:
   #     model = Ocena
    #    fields = ['przedmiot','komentarz']