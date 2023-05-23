from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, null=False)
    numero_chasis = models.CharField(max_length=17, null=False, unique=True)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=10, null=False)
    ultima_revision = models.DateField(null=False)
    proxima_revision = models.DateField(null=False)
    observaciones = models.CharField(max_length=200)