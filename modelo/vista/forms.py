from django import forms
from .models import *

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'contrasena']

class rutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['ruta', 'cp','usuario_id']
