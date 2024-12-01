from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Licitacion, Articulo, Categoria
from .serializers import LicitacionSerializer, ArticuloSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework import status

class LicitacionListCreateView(generics.ListCreateAPIView):
    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        licitacion = self.get_object()
        
        # Verificar que el usuario sea el licitador de la licitación
        if licitacion.licitador != request.user:
            return Response({"error": "No tienes permiso para actualizar esta licitación."}, status=status.HTTP_403_FORBIDDEN)
        
        # Permitir actualizar los campos enviados
        serializer = self.get_serializer(licitacion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(licitador=self.request.user)

class LicitacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Licitacion.objects.all()
    serializer_class = LicitacionSerializer
    permission_classes = [IsAuthenticated]

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

