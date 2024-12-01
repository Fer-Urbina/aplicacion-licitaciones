from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class EscuelaArea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Licitacion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
        ('evaluada', 'Evaluada'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierta')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # Opcional
    licitador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'licitador'})
    area = models.ForeignKey('EscuelaArea', on_delete=models.CASCADE, null=True, blank=True)   # Relación agregada

    def __str__(self):
        return self.titulo

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField()
    unidad = models.CharField(max_length=50, default="unidad")  # Ejemplo: "Piezas"
    licitacion = models.ForeignKey(Licitacion, related_name='articulos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} {self.unidad})"