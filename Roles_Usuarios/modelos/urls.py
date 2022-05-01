
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('',LoginView.as_view(template_name = 'login.html'), name='login'),
    path('salir/',LogoutView.as_view(), name='logout'),
    path("incio/",Inicio.as_view(), name="Index"),
    path("registro-usuario/",CrearUsuario.as_view(), name="registro"),
    path("listar-usuarios/",ListadoUsuarios.as_view(), name="listar_usuarios"),
    path("editar-usuario/<int:pk>",EditarUsuario.as_view(), name="editar_usuario"),
    path("eliminar-usuario/<int:pk>",BorrarUsuario.as_view(), name="eliminar_usuarios")
]
