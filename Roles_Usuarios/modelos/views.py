from django import dispatch
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoUsuarios(ListView):
    model = Usuarios_dePrueva
    template_name = 'usuarios/listado_usuario.html'
    context_object_name = 'listar_usuarios'
    queryset = Usuarios_dePrueva.objects.all()

class EditarUsuario(UpdateView):
    model = Usuarios_dePrueva
    form_class  = usuarioForm
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class CrearUsuario(CreateView):
    model = Usuarios_dePrueva
    form_class = usuarioForm
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class BorrarUsuario(DeleteView):
    model = Usuarios_dePrueva
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
