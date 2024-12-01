from django.urls import path
from .views import PropuestaListCreateView, PropuestasPorLicitacionView, EvaluacionCreateView, EvaluacionListView, MarcarGanadoraView

urlpatterns = [
    path('', PropuestaListCreateView.as_view(), name='propuesta-list-create'),  # Listar y enviar propuestas
    path('<int:licitacion_id>/', PropuestasPorLicitacionView.as_view(), name='propuesta-por-licitacion'), # Ver propuestas de una licitación específica
    path('evaluaciones/', EvaluacionCreateView.as_view(), name='evaluacion-create'),  # Crear evaluación
    path('evaluaciones/<int:propuesta_id>/', EvaluacionListView.as_view(), name='evaluacion-list'),  # Listar evaluaciones de una propuesta
    path('<int:pk>/ganar/', MarcarGanadoraView.as_view(), name='propuesta-ganadora'),  # Ruta para marcar como ganadora
]