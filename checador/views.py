from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import RegistroSerializer
from .serializers import IncidenciaSerializer
from .serializers import MeseSerializer
from .models import Registro
from .models import Incidencia
from .models import Mese

# Create your views here.

class RegistroViewSet(viewsets.ModelViewSet):
    queryset=Registro.objects.all()
    serializer_class=RegistroSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset=Incidencia.objects.all()
    serializer_class=IncidenciaSerializer

class MeseViewSet(viewsets.ModelViewSet):
    queryset=Mese.objects.all()
    serializer_class=MeseSerializer

    
