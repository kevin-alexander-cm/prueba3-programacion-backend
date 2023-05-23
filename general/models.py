from django.db import models

# Create your models here.
class Usuarios(models.Model):
    username = models.CharField(primary_key=True, max_length=25)
    password = models.CharField(max_length=40, null=False, unique=True)
    email = models.CharField(max_length=60, null=False)
    nombre = models.CharField(max_length=60, null=False)
    perfil = models.IntegerField(null=False)