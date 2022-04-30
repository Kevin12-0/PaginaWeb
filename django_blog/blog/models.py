from statistics import mode
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria', max_length= 200, blank= False, null=False)
    estado = models.BooleanField('Categoria Activada/Categoria desactivada',default=True)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=True, auto_now = False)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de autor', max_length=255, blank=False, null=False)
    apellidos = models.CharField('Apellidos de autor', max_length=255, blank=False, null=False)
    facebook = models.URLField('Facebook',null=True, blank=True)
    instagram = models.URLField('Instagram',null=True, blank=True)
    twitter = models.URLField('Twitter',null=True, blank=True)
    pagina_web = models.URLField('Pagina Web',null=True, blank=True)
    correo = models.EmailField('Correo',null=False, blank= False)
    estado = models.BooleanField('Autor Activo/Autor inactivo',default=True)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=True,auto_now = False)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombres)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo de Post', max_length=255, blank= False, null=False)
    slug = models.CharField('Slug', max_length=255, blank= False, null=False)
    descripcion = models.CharField('Descripcion', max_length=100, blank= False, null=False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField('imagen',max_length= 400, blank= False, null=False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion o modificación', auto_now_add=True, auto_now = False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo

