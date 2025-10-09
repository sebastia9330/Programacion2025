from django.db import models

# Modelo para registrar ingresos
class Ingresos(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - ${self.valor}"

class Gastos(models.Model):
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - ${self.valor}"