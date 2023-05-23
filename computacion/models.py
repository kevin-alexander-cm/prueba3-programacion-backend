from django.db import models

# Create your models here.
class InsumosComputacionales(models.Model):
    nro_insumo = models.CharField(primary_key=True, max_length=50, null=False)
    name_insumo = models.CharField(max_length=50, null=False)
    fecha_adquisicion = models.DateField(null=False)
    marca = models.CharField(max_length=30, null=False)
    stock = models.IntegerField(null=False)
    description = models.CharField(max_length=100, null=False)
    

  