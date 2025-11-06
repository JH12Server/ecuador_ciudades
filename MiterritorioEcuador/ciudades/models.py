from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)
    poblacion = models.IntegerField()
    lugares_turisticos = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"
# Create your models here.
