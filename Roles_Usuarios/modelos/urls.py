from django.contrib import admin
from django.urls import path
from .views import index, registrarUsuario,listar_usuarios

urlpatterns = [
    path("index/",index, name="Index"),
    path("registro-usuario/",registrarUsuario, name="registro"),
    path("listar-usuarios/",listar_usuarios, name="listar_usuarios"),
]
