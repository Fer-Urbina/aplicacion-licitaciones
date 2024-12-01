from django.contrib import admin
from .models import Categoria, Licitacion, Articulo, EscuelaArea

# Registrar los modelos de Licitaciones y Artículos
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Licitacion)
class LicitacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio', 'fecha_fin', 'estado', 'licitador']
    list_filter = ['estado', 'categoria', 'fecha_inicio']
    search_fields = ['titulo', 'descripcion']
    fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'categoria', 'licitador', 'area']

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'unidad', 'licitacion']
    list_filter = ['licitacion']
    search_fields = ['nombre', 'descripcion']

@admin.register(EscuelaArea)
class EscuelaAreaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre', 'descripcion']