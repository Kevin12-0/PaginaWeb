from xml.parsers.expat import model
from django import dispatch
from django.shortcuts import render, redirect
from .forms import usuarioForm
from .models import Usuarios
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoUsuarios(ListView):
    model = Usuarios
    template_name = 'usuarios/listado_usuario.html'
    context_object_name = 'listar_usuarios'
    queryset = Usuarios.objects.all()

class EditarUsuario(UpdateView):
    model = Usuarios
    template_name = 'usuarios/registro_usuario.html'
    form_class  = usuarioForm
    success_url = reverse_lazy('listar_usuarios')# nombre de la url

class CrearUsuario(CreateView):
    model = Usuarios
    form_class = usuarioForm
    template_name = 'usuarios/registro_usuario.html'
    success_url = reverse_lazy('registro')# nombre de la url

class BorrarUsuario(DeleteView):
    model = Usuarios
    success_url = reverse_lazy('listar_usuarios')

