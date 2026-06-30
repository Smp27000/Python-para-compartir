from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    nit = models.CharField(max_length=20)
    observaciones = models.CharField(max_length=200)
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'proveedor'