from django import dispatch
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
"""
    TempleteView: es solo para mostrar un templete, no da mas funciones
    ListView: es usado para poder listar tus registros , aunque es nesesario el 
    context_objet_name para poder definile un nombre
    EditView: es para poder editar registros que se hayan hecho, se usa reverse_lazy por que es una forma de 
    redirigir a otra pagina
    DeleteView: es usado para poder elimiar registros

    "Nota": --todas la vistas estan basadas en classes para poder ahorrar codigo, la libreria para eso es
            from django.views.generic import * y para reverse lazay es from django.urls import reverse_lazy ----
"""
class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoUsuarios(ListView):
    model = Usuarios
    template_name = 'usuarios/listado_usuario.html'
    context_object_name = 'listar_usuarios'
    queryset = Usuarios.objects.all()

class EditarUsuario(UpdateView):
    model = Usuarios
    form_class  = usuarioForm
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class CrearUsuario(CreateView):
    model = Usuarios
    form_class = usuarioForm
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class BorrarUsuario(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('listar_usuarios')

# clases de rutas

class ListadoRuta(ListView):
    model = Ruta
    template_name = 'rutas/listado_ruta.html'

class CrearRuta(CreateView):
    model = Ruta
    form_class = rutaForm
    template_name = 'rutas/registro_ruta.html'
    success_url = reverse_lazy('listar_ruta')

class EditarRuta(UpdateView):
    model = Ruta
    form_class = rutaForm
    template_name = 'rutas/registro_ruta.html'
    success_url = reverse_lazy('listar_ruta')

class BorrarRuta(DeleteView):
    model = Ruta
    success_url = reverse_lazy('listar_ruta') 
