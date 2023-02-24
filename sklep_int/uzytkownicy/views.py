from django.shortcuts import render
from .models import Buty,Ocena,Marki
from rest_framework import viewsets
from .serializer import ButySerializer




def index(request):
    but = Buty.objects.all()
    marka = Marki.objects.all() 
    return render(request,"index.html",{'but':but,'marka':marka})



#REST API

class ButyViewSet(viewsets.ModelViewSet):
    queryset = Buty.objects.all()
    serializer_class = ButySerializer


#class OcenaViewSet(viewsets.ModelViewSet):
 #   queryset = Ocena.object.all()
  #  serializer_class = OcenaSerializer