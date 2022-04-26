from django.urls import path
from.views import Home, newUser,listarUsuarios
urlpatterns = [
    path('home/',Home, name = 'Index'),
    path('nuevo_usuario/',newUser, name='Nuevo Usurio'),
    path('listar_usuarios/',listarUsuarios, name='Listar usuarios')
]