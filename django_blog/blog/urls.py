from django.urls import path
from .views import *

urlpatterns = [
     path('',home, name = 'home'),
     path('<slug:slug>/',detallePost,name = 'detalle_post'),
     path('generales/',generales, name = 'generales'),
     path('tecnologia/',tecnologia, name = 'tecnologia'),
     path('videojuegos/',videojuegos,name='videojuegos'),
     path('musica/',musica,name = 'musica'),
     path('tutoriales/',tutoriales,name='tutoriales')
]
