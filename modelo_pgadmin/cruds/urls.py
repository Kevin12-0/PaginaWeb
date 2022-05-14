from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
from usuarios.views import *
"""
    login_requiered se usa para que el usuario pueda acceder a las urls estando forsosamente logeado
    .as_view se usa para llamar a las clases vistas
"""
"""
    todas las urls se ven desde aqui, desde la primer app creada
"""

urlpatterns = [
    path("",Login.as_view(), name="login-2"),
    path("incio/",login_required(Inicio.as_view()), name="Index"),
    path("registro-usuario/",login_required(CrearUsuario.as_view()), name="registro"),
    path("listar-usuarios/",login_required(ListadoUsuarios.as_view()), name="listar_usuarios"),
    path("editar-usuario/<int:pk>",login_required(EditarUsuario.as_view()), name="editar_usuario"),
    path("eliminar-usuario/<int:pk>",login_required(BorrarUsuario.as_view()), name="eliminar_usuarios"),

    path("registro-ruta/",login_required(CrearRuta.as_view()), name="registro_ruta"),
    path("listar-ruta/",login_required(ListadoRuta.as_view()), name="listar_ruta"),
    path('editar-ruta/<int:pk>/',login_required(EditarRuta.as_view()), name="editar_ruta"),
    path('eliminar-ruta/<int:pk>/',login_required(BorrarRuta.as_view()), name="eliminar_ruta"),

    path('crear_usuario/',RegistrarUsuario.as_view(),name="crear_usuario"),
    path('listar-superusers/',login_required(ListadoSuperUsuarios.as_view()),name='listar_superusers'),
    path('editar-super-usuario/<int:pk>/',login_required(EditarSuperUsuario.as_view()),name='editar_SuperUser'),
    path('eliminar-superusuario/<int:pk>/',login_required(EliminarSuperUser.as_view()),name = 'eliminar_SuperUser'),

    path("logout/",login_required(LogoutUsuario),name='logout'),

]
"""
    se cambia el campo id por pk cuando se usan vistas, por que el formato que usa
    django desde su nucleo
"""