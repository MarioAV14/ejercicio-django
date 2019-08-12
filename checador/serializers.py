from rest_framework import serializers
from .models import Registro
from .models import Incidencia
from .models import Mese

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro
        fields=['id', 'hora', 'nombre', 'nivel', 'observacion']

class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incidencia
        fields=['id', 'nombre', 'registros']

class MeseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mese
        fields=['id', 'mes', 'incidencia', 'registro']