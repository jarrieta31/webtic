from django.db import models

# Create your models here.

# Create your models here.
class Destino(models.Model):
    identificador = models.CharField(max_length=100, unique=True, verbose_name="Identificador")

    class Meta():
        verbose_name = 'destino'
        verbose_name_plural = 'destinos'
        ordering = ('identificador',)

    def __str__(self):
        return self.identificador

class Persona(Destino):
    ci = models.CharField(max_length=8, unique=True, verbose_name="Cédula")
    nombre1 = models.CharField(max_length=50, verbose_name="Primer nombre")
    nombre2 = models.CharField(max_length=50, verbose_name="Segundo nombre", null=True, blank=True)
    apellido1 = models.CharField(max_length=50, verbose_name="Primer apellido")
    apellido2 = models.CharField(max_length=50, verbose_name="Segundo apellido", null=True, blank=True)
    email = models.EmailField(verbose_name='Email', null=True, blank=True, unique=True)

    class Meta():
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        return self.ci


class MarcaVehiculo(models.Model):
    marca = models.CharField(max_length=50, verbose_name='Marca', unique=True)

    class Meta():
        verbose_name = 'marca de vehículo'
        verbose_name_plural = 'marcas de vehículos'
        ordering = ('marca',)
    
    def __str__(self):
        return self.marca

class ModeloVehiculo(models.Model):
    modelo = models.CharField(max_length=60, verbose_name='Modelo', unique=True)

    class Meta():
        verbose_name = 'modelo de vehículo'
        verbose_name_plural = 'modelos de vehículos'
        ordering = ('modelo',)

    def __str__(self):
        return self.modelo

class Vehiculo(Destino):
    matricula = models.CharField(max_length=7, unique=True, verbose_name="Matrícula")
    marca = models.ForeignKey(MarcaVehiculo, verbose_name="Marca", on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloVehiculo, verbose_name="Modelo", on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'vehículo'
        verbose_name_plural = 'vehículos'

    def __str__(self):
        return self.matricula

class Unidad(Destino):
    nombre_unidad = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    telefonos = models.CharField(max_length=100, verbose_name="Teléfonos", null=True, blank=True)

    class Meta():
        verbose_name = 'unidad'
        verbose_name_plural = 'unidades'

    def __str__(self):
        return self.nombre_unidad