# Generated by Django 4.0.4 on 2022-04-30 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.URLField(max_length=400, verbose_name='imagen'),
        ),
    ]
