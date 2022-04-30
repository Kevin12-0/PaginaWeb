from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.


def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset)).distinct()
    return render(request, 'index.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'detalle_post': post})


def generales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre__iexact='Generales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Generales')).distinct()

    return render(request, 'generales.html', {'posts': posts})


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre__iexact='Tecnologia'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado=True, categoria=Categoria.objects.get(nombre__iexact='Tecnologia')).distinct()
    return render(request, 'tecnologia.html', {'posts': posts})


def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre__iexact='Videojuegos'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado=True, categoria=Categoria.objects.get(nombre__iexact='Videojuegos')
        ).distinct()
    return render(request, 'videojuegos.html', {'posts': posts})


def musica(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre__iexact='Musica'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado=True, categoria=Categoria.objects.get(nombre__iexact='Musica')
        ).distinct()
    return render(request, 'musica.html', {'posts': posts})


def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado=True, categoria=Categoria.objects.get(nombre__iexact='Tutoriales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset),
            estado=True, categoria=Categoria.objects.get(nombre__iexact='Tutoriales')
        ).distinct()
    return render(request, 'tutoriales.html', {'posts': posts})
