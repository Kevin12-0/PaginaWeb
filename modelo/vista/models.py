from django.db import models
# Create your models here.


class Usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre(s)',max_length= 200, blank= False, null=False)
    apellido = models.CharField('Apellidos',max_length = 200, blank= False, null=False)
    email = models.CharField('Correo',max_length = 200, blank= False, null=False)
    contrasena = models.CharField('Contraseña',max_length = 200, blank= False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=False, auto_now = True)

    class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuario(s)'
        ordering = ['id']
    
    def __str__(self):
        return self.nombre


class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    ruta = models.CharField(max_length=200,blank= False, null=False)
    cp = models.CharField(max_length=5,blank=False, null=False)
    usuario_id = models.OneToOneField(Usuarios, on_delete= models.CASCADE)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=False, auto_now = True)

    class Meta:
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'
        ordering = ['id']

    def __str__(self):
        return self.ruta