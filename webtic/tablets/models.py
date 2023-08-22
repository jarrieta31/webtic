from django.db import models
from equipos.models import Equipo

# Create your models here.

class MarcaTablet(models.Model):
    marca = models.CharField(max_length=60, verbose_name='Marca', unique=True)

    class Meta():
        verbose_name = 'marca tablet'
        verbose_name_plural = 'marcas tablets'
        ordering = ('marca',)

    def __str__(self):
        return self.marca

class ModeloTablet(models.Model):
    modelo = models.CharField(max_length=60, verbose_name='Modelo', unique=True)

    class Meta():
        verbose_name = 'modelo tablet'
        verbose_name_plural = 'modelos tablets'
        ordering = ('modelo',)

    def __str__(self):
        return self.modelo

class Tablet(Equipo):
    marca = models.ForeignKey(MarcaTablet, verbose_name='Marca', on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloTablet, verbose_name='Modelo', on_delete=models.CASCADE)
    imei1 = models.CharField(max_length=15, verbose_name='IMEI 1', unique=True)
    imei2 = models.CharField(max_length=15, verbose_name='IMEI 2', unique=True)
    serie = models.CharField(max_length=15, verbose_name='Nro. Serie', unique=True)
    imagen = models.ImageField(verbose_name="Imagen", upload_to='tablets', null=True, blank=True)
    observaciones = models.TextField(verbose_name='Observaciones', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edidión")

    class Meta():
        verbose_name = 'equipo tablet'
        verbose_name_plural = 'equipos tables'
        ordering = ('serie',)
    
    def __str__(self):
        return self.imei1
