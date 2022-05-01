from django import dispatch
from django.shortcuts import render, redirect
from .forms import usuarioForm
from .models import Usuarios
from django.views.generic import View
# Create your views here.
class Inicio(View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')
def registrarUsuario(request):
    if request.method == 'POST':
        usuarios_form = usuarioForm(request.POST)
        if usuarios_form.is_valid():
            usuarios_form.save()
            return redirect('Index')
    else:
        usuarios_form = usuarioForm
    return render(request, 'usuarios/registro_usuario.html',{'usuarios_form':usuarios_form})
def listar_usuarios(request):
    context = {'listar_usuarios': Usuarios.objects.all()}
    return render(request, 'usuarios/listado_usuario.html',context)
def editar_usuario(request,id=0): 
    if request.method == 'GET':
        if id == 0:
            usuarios_form = usuarioForm()
        else:
            usuario = Usuarios.objects.get(pk=id)
            usuarios_form = usuarioForm(instance=usuario)
        return render (request, 'usuarios/registro_usuario.html',{'usuarios_form':usuarios_form})
    else:
        if id == 0:
            usuarios_form = usuarioForm(request.POST)
        else:
            usuario = Usuarios.objects.get(pk=id)
            usuarios_form = usuarioForm(request.POST,instance=usuario)
        if usuarios_form.is_valid():
            usuarios_form.save()
    return redirect('listar_usuarios')
def eliminar_usuarios(request, id):
    usuario= Usuarios.objects.get(pk=id)
    usuario.delete()
    return redirect('listar_usuarios')