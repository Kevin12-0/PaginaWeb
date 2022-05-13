import email
from django.db import models
from django.contrib.auth.models import *


class UsuairoManager(BaseUserManager):
    """
        se define en una sierta parte como se va a comportar el formulario, y que campos son los que se pedirian
        para realizar el registro de una manera exitosa,
        ademas de que no permite que el usuario o la contraseña sean iguales o similares
    """
    def create_user(self, email, username, nombres, apellidos, password=None):
        if not email:
            raise ValueError('El correo electronico es necesario')
        usuario = self.model(username=username, email=self.normalize_email(
            email), nombres=nombres, apellidos=apellidos)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, apellidos, password):
        """
            creacion de super usuario, por el momento solo se hace desde consola, si se queire hacer desde
            un template, lo unicao que se nesesitas es mandar a llamar el campo dentro de la funcion 
            create_user
        """
        usuario = self.create_user(
            email, username=username, nombres=nombres, apellidos=apellidos, password=password)
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    """
        modelo de usuario,
        para guardar imagen es nesesario instlar pillow
        la clave primaria es PK, ya que django la asigno de manera automatica
    """
    username = models.CharField(
        'UserName', unique=True, max_length=50)
    email = models.EmailField('Correo', unique=True,
                              max_length=200)
    nombres = models.CharField(
        'Nombre(s)', max_length=150, blank=True, null=True)
    apellidos = models.CharField(
        'Apellidos', max_length=150, blank=True, null=True)
    imagen = models.ImageField('Imagen de perfil', upload_to='images/',
                               max_length=255, blank=True, null=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = UsuairoManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres}, {self.apellidos}'

        """
            estas 3 funciones definnen los permisos de los usuarios
        """

    def has_perm(self, perm, object=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador