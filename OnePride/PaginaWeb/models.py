from django.db import models

# Create your models here.
<<<<<<< Updated upstream
=======
class Servicio(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripción = models.CharField(max_length=150)
    costo = models.PositiveIntegerField(default=0)
>>>>>>> Stashed changes
