from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol', 'telefono']  # Campos del perfil
        read_only_fields = ['id', 'username', 'rol']  # Evitamos que estos se modifiquen

    def create(self, validated_data):
        # Método para la creación de usuarios en el registro
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            rol=validated_data['rol'],  # El rol debe especificarse aquí
            telefono=validated_data.get('telefono', None),
            password=validated_data['password']
        )
        return user

    def validate_rol(self, value):
        # Validación personalizada del rol
        if value not in ['licitador', 'proveedor']:
            raise serializers.ValidationError("El rol debe ser 'licitador' o 'proveedor'.")
        return value
    
    def validate_email(self, value):
        if not "@" in value:
            raise serializers.ValidationError("Por favor, ingresa un correo válido.")
        return value

    def validate_telefono(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("El teléfono solo debe contener números.")
        return value
