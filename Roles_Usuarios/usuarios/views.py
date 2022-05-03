from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils.decorators import *
from django.views.decorators.cache import *
from django.views.decorators.csrf import *
from .forms import *
from django.urls import *

class LoginView(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
