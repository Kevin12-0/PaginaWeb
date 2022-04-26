from django.shortcuts import render, redirect
from .forms import usuarioForm
from .models import Usuarios
# Create your views here.
def index(request):
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
    

