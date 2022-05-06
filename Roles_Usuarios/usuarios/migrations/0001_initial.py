# Generated by Django 4.0.4 on 2022-05-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='UserName')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Correo')),
                ('nombres', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre(s)')),
                ('apellidos', models.CharField(blank=True, max_length=150, null=True, verbose_name='Apellidos')),
                ('imagen', models.ImageField(blank=True, max_length=255, null=True, upload_to='images/', verbose_name='Imagen de perfil')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
