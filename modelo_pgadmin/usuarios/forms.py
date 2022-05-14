from dataclasses import fields
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

"""
    Formulario login, define como tal el tipo de formulario que se usara para el inicio de sesion
"""
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
    
    def clean_password2(self):
        """
            este es el metodo para validar que ambas contraseñas sean
            igules

            validartionError si las contraseñas no coninciden 
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit= False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user