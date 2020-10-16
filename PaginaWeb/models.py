from django.db import models

# Create your models here.
class Servicio(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripción = models.CharField(max_length=200)
    costo = models.PositiveIntegerField(max_lenght=10)