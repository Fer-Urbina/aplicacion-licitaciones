from .settings import *  # Importar toda la configuración base

DEBUG = False  # Desactiva el modo DEBUG para producción

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # Cambia esto según el dominio o IP de tu servidor en producción

# Configuración de base de datos para producción
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# Configuración de seguridad
SECURE_HSTS_SECONDS = 31536000  # Habilitar HSTS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True