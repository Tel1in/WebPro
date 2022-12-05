from django.db import models


# Create your models here.


class Clientes(models.Model):
    id=models.CharField(primary_key=True, max_length=10)
    nombre=models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    edad = models.SmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.id)
