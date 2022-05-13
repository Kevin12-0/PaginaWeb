from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.utils.decorators import *
from django.views.decorators.cache import *
from django.views.decorators.csrf import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from .forms import *
from django.urls import *
from django.views.generic import *
from .models import *
from .forms import *
class Login(FormView):
    """
        logica del login tomando como referencia nucleo django y usuando csrf_token,
        todo se tienen que hacer mediante decoradores y mediante clases
        DECORADORES
        from django.views.decorators.cache import *
        from django.views.decorators.csrf import *
    """

    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Index')

    @method_decorator(csrf_protect) #decorador 
    @method_decorator(never_cache) # decprador
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def LogoutUsuario(request):
    logout(request)
    return redirect('login-2')

"""
    cruds para los usuarios, bassandonos en la logica de las vistas
"""
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'signup.html'
    success_url = reverse_lazy('login-2')
class ListadoSuperUsuarios(ListView):
    model = Usuario
    template_name = 'superusuarios/listado_superuser.html'
    queryset = Usuario.objects.filter(usuario_activo = True)

class EditarSuperUsuario(UpdateView):
    model = Usuario
    form_class  = FormularioUsuario
    template_name = 'signup.html'
    success_url = reverse_lazy('listar_superusers')# nombre de la url

class EliminarSuperUser(DeleteView):
    model = Usuario
    success_url = reverse_lazy('listar_superusers')