# Generated by Django 4.1.1 on 2022-09-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Especialidad', models.CharField(max_length=50)),
                ('Jornada', models.CharField(max_length=15)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
