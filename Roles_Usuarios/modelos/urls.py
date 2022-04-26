from django.contrib import admin
from django.urls import path
from .views import index, registrarUsuario,listar_usuarios,editar_usuario,eliminar_usuarios

urlpatterns = [
    path("index/",index, name="Index"),
    path("registro-usuario/",registrarUsuario, name="registro"),
    path("listar-usuarios/",listar_usuarios, name="listar_usuarios"),
    path("editar-usuario/<int:id>",editar_usuario, name="editar_usuario"),
    path("eliminar-usuario/<int:id>",eliminar_usuarios, name="eliminar_usuarios")
]
