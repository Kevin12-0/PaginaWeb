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

def registrarUsuario(request):
    if request.method == 'POST':
        usuarios_form = usuarioForm(request.POST)
        if usuarios_form.is_valid():
            usuarios_form.save()
            return redirect('Index')
    else:
        usuarios_form = usuarioForm
    return render(request, 'usuarios/registro_usuario.html',{'usuarios_form':usuarios_form})

def eliminar_usuarios(request, id):
    usuario= Usuarios.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios')