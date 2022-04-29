from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')
def generales(request):
    return render(request, 'generales.html')
def tecnologia(request):
    return render(request, 'tecnologia.html')
def videojuegos(request):
    return render(request, 'videojuegos.html')
def musica(request):
    return render(request, 'musica.html')   
    
