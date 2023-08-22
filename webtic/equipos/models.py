from django.db import models
from destinos.models import Destino


#class TipoEquipo(models.Model):
#    tipo = models.CharField(max_length=50, verbose_name="Tipo de equipo", unique=True)
#
#    class Meta():
#        verbose_name = 'tipo equipo'
#        verbose_name = 'tipos de equipos'
#        ordering = ('tipo',)
#    
#    def __str__(self):
#        return self.tipo

class Equipo(models.Model):
#    tipo = models.ForeignKey(TipoEquipo, verbose_name="Tipo de equipo", on_delete=models.CASCADE)
    item = models.CharField(max_length=25, verbose_name='Nro. Inventario', null=True, blank=True, unique=True)
    ubicacion = models.ForeignKey(Destino, verbose_name="Ubicación", on_delete=models.CASCADE) 

    class Meta():
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'
        ordering = ('item',) 


