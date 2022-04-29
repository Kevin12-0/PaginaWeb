from django.urls import path
from .views import *

urlpatterns = [
     path('',home, name = 'home'),
     path('generales/',generales, name = 'generales'),
     path('tecnologia/',tecnologia, name = 'tecnologia'),
     path('videojuegos/',videojuegos,name='videojuegos'),
]
