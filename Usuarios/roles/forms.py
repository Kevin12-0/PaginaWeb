from django import forms
from .models import usuaios
class usuarioform(forms.ModelForm):
    class Meta:
        model = usuaios
        fields = ['Nombre', 'apellido', 'email', 'contrasena']
        