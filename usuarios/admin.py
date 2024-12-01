from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Personalizar la visualización del modelo de Usuario en el admin
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('rol', 'telefono')}),
    )
    list_display = ['username', 'email', 'rol', 'is_staff']

admin.site.register(Usuario, CustomUserAdmin)