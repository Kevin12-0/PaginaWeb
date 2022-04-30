from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request, 'index.html', {'posts': posts})

def detallePost(request,slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'post.html',{'detalle_post':post})

def generales(request):
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre='Generales'))
    return render(request, 'generales.html', {'posts': posts})


def tecnologia(request):
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre='Tecnologia'))
    return render(request, 'tecnologia.html', {'posts': posts})


def videojuegos(request):
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre='Videojuegos'))
    return render(request, 'videojuegos.html', {'posts': posts})


def musica(request):
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre='Musica'))
    return render(request, 'musica.html', {'posts': posts})


def tutoriales(request):
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre='Tutoriales'))
    return render(request, 'tutoriales.html', {'posts': posts})
