from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.utils.decorators import *
from django.views.decorators.cache import *
from django.views.decorators.csrf import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from .forms import *
from django.urls import *

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('Index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
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
