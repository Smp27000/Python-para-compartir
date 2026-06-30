from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    celular = models.CharField(max_length=12)
    email = models.CharField(max_length=45)

    class Meta:
        db_table = 'cliente'
