from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    nit = models.CharField(max_length=20)
    observaciones = models.CharField(max_length=200)
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'proveedor'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto'