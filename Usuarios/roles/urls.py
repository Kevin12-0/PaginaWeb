from django.urls import path
from.views import Home, newUser
urlpatterns = [
    path('home/',Home, name = 'Index'),
    path('nuevo_usuario/',newUser, name='Nuevo Usurio')
]