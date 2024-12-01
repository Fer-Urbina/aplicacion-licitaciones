# Sistema de Gestión de Licitaciones

Este es un sistema diseñado para gestionar el proceso de licitaciones, donde los licitadores pueden publicar licitaciones y los proveedores pueden enviar propuestas. Además, permite evaluar propuestas y seleccionar un proveedor ganador.

## Funcionalidades Principales

### Usuarios
- **Registro de usuarios**: Los usuarios pueden registrarse especificando su rol (Licitador o Proveedor).
- **Inicio de sesión**: Autenticación mediante JWT para proteger los endpoints.
- **Perfil de usuario**: Cada usuario puede ver y actualizar su perfil.

### Gestión de Licitaciones (Licitador)
- Crear nuevas licitaciones.
- Listar licitaciones abiertas (visible para ambos roles).
- Actualizar licitaciones (ejemplo: cerrar una licitación).
- Consultar los detalles de una licitación específica.

### Recepción de Propuestas (Proveedor)
- Enviar propuestas para licitaciones abiertas.
- Consultar las propuestas enviadas.

### Evaluación de Propuestas (Licitador)
- Evaluar propuestas recibidas.
- Consultar evaluaciones realizadas.
- Seleccionar al proveedor ganador.

## Tecnologías Utilizadas
- **Backend**: Django y Django REST Framework.
- **Base de Datos**: SQLite (por defecto, puedes cambiarla a PostgreSQL o MySQL).
- **Autenticación**: JWT (JSON Web Tokens) usando `rest_framework_simplejwt`.

## Configuración del Proyecto

### Requisitos Previos
- Python 3.9 o superior.
- Git.
- Un entorno virtual configurado.

### Instalación
1. Clona este repositorio:
   
  Crea y activa un entorno virtual:

## Instalación y Configuración

## Instalación y Configuración

### Crea y activa un entorno virtual:

python -m venv env
source env/bin/activate   # En Linux/Mac
env\Scripts\activate      # En Windows

### Instala las dependencias:
pip install -r requirements.txt

### Realiza las migraciones:
python manage.py makemigrations
python manage.py migrate

### Inicia el servidor de desarrollo:
python manage.py runserver
Accede a la aplicación en tu navegador en: http://127.0.0.1:8000.

### Datos de Usuario para Pruebas
Puedes crear usuarios desde el admin de Django:
python manage.py createsuperuser

### Endpoints del API
## Usuarios
Registro: /api/usuarios/ (POST)
Inicio de Sesión: /api/token/ (POST)
Ver Perfil: /api/usuarios/perfil/ (GET)
Actualizar Perfil: /api/usuarios/perfil/ (PATCH)
## Licitaciones
Crear Licitación: /api/licitaciones/ (POST)
Listar Licitaciones: /api/licitaciones/ (GET)
Detalles de una Licitación: /api/licitaciones/<id>/ (GET)
Actualizar Licitación: /api/licitaciones/<id>/ (PATCH)
## Propuestas
Enviar Propuesta: /api/propuestas/ (POST)
Listar Propuestas por Licitación: /api/propuestas/<id_licitacion>/ (GET)
## Evaluaciones
Crear Evaluación: /api/propuestas/evaluaciones/ (POST)
Consultar Evaluaciones: /api/propuestas/evaluaciones/<id_propuesta>/ (GET)
## Seleccionar Proveedor Ganador
Marcar como Ganadora: /api/propuestas/<id_propuesta>/ganar/ (POST)

### Contribuciones
Si deseas contribuir al proyecto, crea un fork, realiza tus cambios en una rama nueva y envía un pull request.

### Autor
## Fernando Urbina
Proyecto desarrollado como parte de un sistema de gestión de licitaciones.










   
