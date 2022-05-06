# Generated by Django 4.0.4 on 2022-05-06 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vista', '0002_rename_usuarios_deprueva_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.CharField(max_length=200)),
                ('cp', models.CharField(max_length=5)),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='Fecha de creacion o modificación')),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vista.usuarios')),
            ],
            options={
                'verbose_name': 'ruta',
                'verbose_name_plural': 'rutas',
                'ordering': ['id'],
            },
        ),
    ]
