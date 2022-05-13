from django import forms
from .models import *

"""
    forms de prueba para realizar cruds desde un usuario registrado
"""
class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'contrasena']

class rutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['ruta', 'cp','usuario_id']
