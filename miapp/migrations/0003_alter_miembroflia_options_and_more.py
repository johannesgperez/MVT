# Generated by Django 4.0 on 2022-04-18 01:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_remove_miembroflia_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miembroflia',
            options={'ordering': ['-edad']},
        ),
        migrations.AddField(
            model_name='miembroflia',
            name='fecha_ingreso_bd',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 22, 6, 47, 957895)),
        ),
    ]
