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
    model = Usuarios
    template_name = 'listado_usuario.html'
    context_object_name = 'listar_usuarios'
    queryset = Usuarios.objects.all()

class EditarUsuario(UpdateView):
    model = Usuarios
    template_name = 'registro_usuario.html'
    form_class  = usuarioForm
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class CrearUsuario(CreateView):
    model = Usuarios
    form_class = usuarioForm
    template_name = 'registro_usuario.html'
    success_url = reverse_lazy('registro')# nombre de la url

class BorrarUsuario(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('listar_usuarios')

# clases de rutas

class ListadoRuta(ListView):
    model = Ruta
    template_name = 'registro_ruta.html'
    context_object_name = 'listar_rutas'
    queryset = Ruta.objects.all()

class ListadoRuta(ListView):
    model = Ruta
    template_name = 'registro_ruta.html'
    form_class = rutaForm
    queryset = Ruta.objects.all()
class CrearRuta(CreateView):
    model = Ruta
    form_class = rutaForm
    template_name = 'registro_ruta.html'
    success_url = reverse_lazy('registro_ruta')

