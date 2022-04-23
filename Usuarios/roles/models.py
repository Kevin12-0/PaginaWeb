from django.db import models

# Create your models here.

class usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre(s)',max_length= 200, blank= False, null=False)
    apellido = models.CharField('Apellidos',max_length = 200, blank= False, null=False)
    email = models.CharField('Correo',max_length = 200, blank= False, null=False)
    contrasena = models.CharField('Contraseña',max_length = 200, blank= False, null=False)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuario(s)'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre