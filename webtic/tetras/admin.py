from django.contrib import admin
from .models import Tetra, TipoTetra, MarcaTetra, ModeloTetra

# Register your models here.
class TetraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'issi', 'tei', 'serie',)
    search_fields = ('nombre', 'issi', 'tei', 'serie',)
    ordering = ('issi',)
    list_filter = ('modelo__modelo',)

class MarcaTetraAdmin(admin.ModelAdmin):
    list_display = ('marca',)
    ordering = ('marca',)

class ModeloTetraAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
    ordering = ('modelo',)

class TipoTetraAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    ordering = ('tipo',)



# admin tetras
admin.site.register(MarcaTetra, MarcaTetraAdmin)
admin.site.register(ModeloTetra, ModeloTetraAdmin)
admin.site.register(TipoTetra, TipoTetraAdmin)
admin.site.register(Tetra, TetraAdmin)