from django.contrib import admin
from .models import *

"""
    modeloes registrados en admin, por si llega a fallar la base de datos
    dentro del admin se puede llegar a realziar un proceso de guardado
"""
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Ruta)