from django.db import models

# Create your models here.
class Registro(models.Model):
    hora=models.DateTimeField(auto_now=False, auto_now_add=False)
    nombre=models.CharField(max_length=50)
    nivel=models.IntegerField()
    observacion=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Incidencia(models.Model):
    nombre=models.CharField(max_length=50)
    registros=models.ForeignKey("Registro", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Mese(models.Model):
    mes=models.CharField(max_length=50)
    incidencia=models.ForeignKey("Incidencia", on_delete=models.CASCADE)
    def __str__(self):
        return self.mes    