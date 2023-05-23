from django.db import models

# Create your models here.
class InsumosOficina(models.Model):
    nro_article = models.CharField(primary_key=True, max_length=50, null=False)
    name_article = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=25, null=False)
    stock = models.IntegerField(null=False)
    description = models.CharField(max_length=100, null=False)
    

    def __str__(self):
        return self.name_article