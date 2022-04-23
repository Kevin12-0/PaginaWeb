from django.db import models

# Create your models here.

class usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 200, blank= False, null=False)
    apellido = models.CharField(max_length = 200, blank= False, null=False)
    email = models.CharField(max_length = 200, blank= False, null=False)
    contrasena = models.CharField(max_length = 200, blank= False, null=False)