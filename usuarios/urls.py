from django.urls import path
from .views import UsuarioListCreateView, PerfilUsuarioView

urlpatterns = [
    path('', UsuarioListCreateView.as_view(), name='usuarios-list-create'),
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil-usuario'),
]