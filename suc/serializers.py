from rest_framework import serializers
from .models import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sucursal
        fields=['id', 'ciudad', 'sucursal', 'slug']