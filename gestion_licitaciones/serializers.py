from rest_framework import serializers
from .models import Licitacion, Articulo, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class LicitacionSerializer(serializers.ModelSerializer):
    articulos = ArticuloSerializer(many=True, read_only=True)

    class Meta:
        model = Licitacion
        fields = ['id', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'estado', 'categoria', 'licitador', 'area', 'articulos']
        read_only_fields = ['id', 'licitador']  # No se puede cambiar el licitador una vez creada la licitación