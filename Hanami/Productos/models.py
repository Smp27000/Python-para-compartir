from django.db import models
from Proveedores.models import Proveedor
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20, default='0')
    fecha = models.CharField(max_length=20)
    foto = models.CharField(max_length=100, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto'