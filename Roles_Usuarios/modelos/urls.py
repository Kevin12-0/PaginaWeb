from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",Inicio.as_view(), name="Index"),
    path("registro-usuario/",CrearUsuario.as_view(), name="registro"),
    path("listar-usuarios/",ListadoUsuarios.as_view(), name="listar_usuarios"),
    path("editar-usuario/<int:pk>",EditarUsuario.as_view(), name="editar_usuario"),
    path("eliminar-usuario/<int:id>",eliminar_usuarios, name="eliminar_usuarios")
]
