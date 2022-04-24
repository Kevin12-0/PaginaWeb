from django import forms
from .models import usuarios

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ['nombre', 'apellido', 'email', 'contrasena']
        