from django.contrib import admin
from .models import Propuesta, Evaluacion

# Registrar los modelos de Propuestas y Evaluaciones
@admin.register(Propuesta)
class PropuestaAdmin(admin.ModelAdmin):
    list_display = ['licitacion', 'proveedor', 'precio', 'fecha_presentacion']
    list_filter = ['licitacion', 'proveedor']
    search_fields = ['descripcion']

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['propuesta', 'puntaje_tecnico', 'puntaje_economico']
    list_filter = ['propuesta__licitacion']
    search_fields = ['comentarios']