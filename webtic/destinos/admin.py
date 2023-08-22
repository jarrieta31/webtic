from django.contrib import admin
from .models import Persona, Unidad, Vehiculo, MarcaVehiculo, ModeloVehiculo

# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('ci','nombre1', 'nombre2', 'apellido1', 'apellido2',)
    search_fields = ('ci','nombre1', 'nombre2', 'apellido1','apellido2',)

class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_unidad', 'get_destino', 'telefonos')
    search_fields = ('nombre_unidad',)
    ordering = ('nombre_unidad',)

    def get_destino(self, obj):
        return ", ".join([obj.identificador.get('identificador')])

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'modelo',)
    search_fields = ('matricula', 'marca', 'modelo',)
    ordering = ('marca', 'modelo', 'matricula',)

# admin destinos
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)