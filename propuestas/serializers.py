from rest_framework import serializers
from .models import Propuesta, Evaluacion

class PropuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propuesta
        fields = ['id', 'licitacion', 'proveedor', 'descripcion', 'precio', 'fecha_presentacion', 'ganadora']  # Incluye 'ganadora'
        read_only_fields = ['id', 'proveedor', 'fecha_presentacion', 'ganadora']  # 'ganadora' es de solo lectura

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ['id', 'propuesta', 'puntaje_tecnico', 'puntaje_economico', 'comentarios']
        read_only_fields = ['id']

    def validate(self, data):
        if data['puntaje_tecnico'] < 0 or data['puntaje_tecnico'] > 100:
            raise serializers.ValidationError({'puntaje_tecnico': 'El puntaje técnico debe estar entre 0 y 100.'})
        if data['puntaje_economico'] < 0 or data['puntaje_economico'] > 100:
            raise serializers.ValidationError({'puntaje_economico': 'El puntaje económico debe estar entre 0 y 100.'})
        return data