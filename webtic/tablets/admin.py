from django.contrib import admin
from .models import MarcaTablet, ModeloTablet, Tablet

# Register your models here.
class MarcaTabletAdmin(admin.ModelAdmin):
    list_display = ('marca',)
    ordering = ('marca',)

class ModeloTabletAdmin(admin.ModelAdmin):
    list_display = ('modelo',)
    ordering = ('modelo',)

class TabletAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo','imei1','imei2',)
    ordering = ('marca','modelo', 'imei1',)

# admin tablets
admin.site.register(MarcaTablet, MarcaTabletAdmin)
admin.site.register(ModeloTablet, ModeloTabletAdmin)
admin.site.register(Tablet, TabletAdmin)