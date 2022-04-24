from hashlib import blake2b
from django.db import models

# Create your models here.

class usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre(s)',max_length= 200, blank= False, null=False)
    apellido = models.CharField('Apellidos',max_length = 200, blank= False, null=False)
    email = models.CharField('Correo',max_length = 200, blank= False, null=False)
    contrasena = models.CharField('Contraseña',max_length = 200, blank= False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=False, auto_now = True)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuario(s)'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class ruta(models.Model):
    id = models.AutoField(primary_key=True)
    ruta = models.CharField('Ruta',max_length=200,blank= False, null=False)
    usuario_id = models.OneToOneField(usuarios, on_delete= models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=False, auto_now = True)

    class Meta:
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'
        ordering = ['ruta']

    def __str__(self):
        return self.ruta
