from django.db import models
from gestion_licitaciones.models import Licitacion
from usuarios.models import Usuario

class Propuesta(models.Model):
    licitacion = models.ForeignKey(Licitacion, related_name='propuestas', on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'proveedor'})
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fecha_presentacion = models.DateTimeField(auto_now_add=True)
    ganadora = models.BooleanField(default=False)  # Nuevo campo para indicar la propuesta ganadora

    def __str__(self):
        return f"Propuesta de {self.proveedor.username} para {self.licitacion.titulo}"

class Evaluacion(models.Model):
    propuesta = models.OneToOneField(Propuesta, on_delete=models.CASCADE)
    puntaje_tecnico = models.PositiveIntegerField()
    puntaje_economico = models.PositiveIntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def puntaje_total(self):
        return self.puntaje_tecnico + self.puntaje_economico

    def __str__(self):
        return f"Evaluación de {self.propuesta.proveedor.username} para {self.propuesta.licitacion.titulo}"