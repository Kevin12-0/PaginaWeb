from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    """
        formulario de registro de un usario desde la base de datos
        variables a usar:
            - password1: contraseña
            - password2: verificacion de contraseña 
    """
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id':'password1',
            'required': 'required',
        }))
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirme su contraseña',
            'id':'password2',
            'required': 'required',
    }))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo electronico',
                    }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre(s)',
                    }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de ususario',
                }
            )

        }

        