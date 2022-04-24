from statistics import mode
from django.shortcuts import render, redirect
from .forms import usuarioForm
def Home(request):
    return render(request,'index.html')

def newUser(request):
    if request.method == 'POST':
        usuarios_form = usuarioForm(request.POST)
        if usuarios_form.is_valid():
            usuarios_form.save()
            return render('index')
    else:
        usuarios_form = usuarioForm
    return render(request,'nuevo_usuario.html',{'usuarios_form':usuarios_form})
