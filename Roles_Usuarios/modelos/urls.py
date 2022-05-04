
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from usuarios.views import *

urlpatterns = [
    #path('salir/',login_required(LogoutView.as_view()), ),
    path("incio/",login_required(Inicio.as_view()), name="Index"),
    path("registro-usuario/",login_required(CrearUsuario.as_view()), name="registro"),
    path("listar-usuarios/",login_required(ListadoUsuarios.as_view()), name="listar_usuarios"),
    path("editar-usuario/<int:pk>",login_required(EditarUsuario.as_view()), name="editar_usuario"),
    path("eliminar-usuario/<int:pk>",login_required(BorrarUsuario.as_view()), name="eliminar_usuarios"),
    path("registro-ruta/",login_required(CrearRuta.as_view()), name="registro_ruta"),
    path("listar-ruta/",login_required(ListadoRuta.as_view()), name="listar_ruta"),
    path("logout/",login_required(LogoutUsuario),name='logout'),
    path("",Login.as_view(), name="login-2"),
]
