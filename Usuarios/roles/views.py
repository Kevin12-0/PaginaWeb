from django.http import HttpResponse

def index(request):
    messaje = 'Hola Mundo'
    return HttpResponse(messaje)

