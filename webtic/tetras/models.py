from django.db import models
from equipos.models import Equipo

# Create your models here.

class MarcaTetra(models.Model):
    marca = models.CharField(max_length=60, verbose_name='Marca', unique=True)

    class Meta():
        verbose_name = 'marca tetra'
        verbose_name_plural = 'marcas tetra'
        ordering = ('marca',)

    def __str__(self):
        return self.marca

class ModeloTetra(models.Model):
    modelo = models.CharField(max_length=60, verbose_name='Modelo', unique=True)

    class Meta():
        verbose_name = 'modelo tetra'
        verbose_name_plural = 'modelos tetra'
        ordering = ('modelo',)

    def __str__(self):
        return self.modelo

class TipoTetra(models.Model):
    tipo = models.CharField(max_length=60, verbose_name='Tipo', unique=True)

    class Meta():
        verbose_name = 'tipo tetra'
        verbose_name_plural = 'tipos tetra'
        ordering = ('tipo',)

    def __str__(self):
        return self.tipo

class Tetra(Equipo):
    nombre = models.CharField(max_length=15, verbose_name='Nombre', unique=True)
    marca = models.ForeignKey(MarcaTetra, verbose_name='Marca', on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloTetra, verbose_name='Modelo', on_delete=models.CASCADE)
    issi = models.CharField(max_length=5, verbose_name='ISSI', unique=True)
    tei = models.CharField(max_length=15, verbose_name='TEI', unique=True)
    serie = models.CharField(max_length=15, verbose_name='Nro. Serie', unique=True)
    observaciones = models.TextField(verbose_name='Observaciones')
    imagen = models.ImageField(verbose_name="Imagen", upload_to='tetras', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edidión")

    class Meta():
        verbose_name = 'equipo tetra'
        verbose_name_plural = 'equipos tetra'
        ordering = ('issi', 'tei',)

    def __str__(self):
        return self.nombre