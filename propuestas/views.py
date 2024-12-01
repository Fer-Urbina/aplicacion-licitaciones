from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics
from .models import Propuesta, Evaluacion
from .serializers import PropuestaSerializer, EvaluacionSerializer
from gestion_licitaciones.models import Licitacion
from rest_framework import status

class PropuestaListCreateView(generics.ListCreateAPIView):
    queryset = Propuesta.objects.all()
    serializer_class = PropuestaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        licitacion_id = self.kwargs.get('licitacion_id')

        if user.rol == 'proveedor':
            return Propuesta.objects.filter(proveedor=user)  # Propuestas enviadas por el proveedor
        elif user.rol == 'licitador' and licitacion_id:
            return Propuesta.objects.filter(licitacion__id=licitacion_id)  # Propuestas para una licitación específica
        return Propuesta.objects.none()  # No debería llegar aquí

    def perform_create(self, serializer):
        user = self.request.user
        if user.rol != 'proveedor':
            raise PermissionError("Solo los proveedores pueden enviar propuestas.")
        licitacion_id = self.request.data.get('licitacion')
        licitacion = Licitacion.objects.get(id=licitacion_id)
        serializer.save(proveedor=user, licitacion=licitacion)

class PropuestasPorLicitacionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, licitacion_id):
        user = request.user
        if user.rol != 'licitador':
            raise PermissionDenied("Solo los licitadores pueden ver las propuestas.")
        
        propuestas = Propuesta.objects.filter(licitacion__id=licitacion_id)
        serializer = PropuestaSerializer(propuestas, many=True)
        return Response(serializer.data)
    
class EvaluacionCreateView(generics.CreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        propuesta_id = self.request.data.get('propuesta')
        propuesta = Propuesta.objects.get(id=propuesta_id)
        if not self.request.user.rol == 'licitador':
            raise PermissionError("Solo los licitadores pueden evaluar propuestas.")
        serializer.save()

class EvaluacionListView(generics.ListAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        propuesta_id = self.kwargs.get('propuesta_id')
        if propuesta_id:
            return Evaluacion.objects.filter(propuesta__id=propuesta_id)
        return super().get_queryset()
    
class MarcarGanadoraView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            propuesta = Propuesta.objects.get(id=pk)
        except Propuesta.DoesNotExist:
            return Response({"error": "Propuesta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Verificar que el usuario sea el licitador de la licitación asociada
        if request.user != propuesta.licitacion.licitador:
            return Response({"error": "No tienes permiso para marcar esta propuesta como ganadora."}, status=status.HTTP_403_FORBIDDEN)

        # Marcar todas las propuestas como no ganadoras y esta como ganadora
        Propuesta.objects.filter(licitacion=propuesta.licitacion).update(ganadora=False)
        propuesta.ganadora = True
        propuesta.save()

        # Actualizar el estado de la licitación
        propuesta.licitacion.estado = "evaluada"
        propuesta.licitacion.save()

        return Response({"message": "Propuesta marcada como ganadora exitosamente."}, status=status.HTTP_200_OK)