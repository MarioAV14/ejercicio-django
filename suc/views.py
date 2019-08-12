from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import SucursalSerializer
from .models import Sucursal

# Create your views here.

class SucursalViewSet(viewsets.ModelViewSet):
    queryset=Sucursal.objects.all()
    serializer_class=SucursalSerializer