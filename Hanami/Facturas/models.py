from django.db import models

from Productos.models import Producto as Productos
from Clientes.models import Cliente

class Factura(models.Model):
    fecha = models.CharField(max_length=10)
    cantidad = models.FloatField()
    precio = models.FloatField()
    total = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, db_column='producto_id1')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_idcliente')

    class Meta:
        db_table = 'factura'
