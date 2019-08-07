from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Registro(models.Model):
    hora=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    nombre=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_registro')
    nivel=models.IntegerField()
    observacion=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre.username
    
class Incidencia(models.Model):
    nombre=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_incidencia')
    registros=models.ForeignKey("Registro", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre.username

class Mese(models.Model):
    mes=models.CharField(max_length=50)
    incidencia=models.ManyToManyField("Incidencia")
    registro=models.OneToOneField("Registro", on_delete=models.CASCADE)
    def __str__(self):
        return self.mes    