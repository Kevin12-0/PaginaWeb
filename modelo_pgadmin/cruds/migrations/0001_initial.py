# Generated by Django 4.0.4 on 2022-05-14 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre(s)')),
                ('apellido', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('email', models.CharField(max_length=200, verbose_name='Correo')),
                ('contrasena', models.CharField(max_length=200, verbose_name='Contraseña')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion o modificación')),
            ],
            options={
                'verbose_name': 'Usuarios',
                'verbose_name_plural': 'Usuario(s)',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.CharField(max_length=200)),
                ('cp', models.CharField(max_length=5)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion o modificación')),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cruds.usuarios')),
            ],
            options={
                'verbose_name': 'ruta',
                'verbose_name_plural': 'rutas',
                'ordering': ['id'],
            },
        ),
    ]
