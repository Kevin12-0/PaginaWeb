from django import forms
from .models import Usuarios

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'contrasena']