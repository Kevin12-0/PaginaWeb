from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    posts = Post.objects.filter(estado = False)
    return render(request, 'index.html',{'posts':posts})
def generales(request):
    return render(request, 'generales.html')
def tecnologia(request):
    return render(request, 'tecnologia.html')
def videojuegos(request):
    return render(request, 'videojuegos.html')
def musica(request):
    return render(request, 'musica.html') 
def tutoriales(request):
    return render(request, 'tutoriales.html')  
    
