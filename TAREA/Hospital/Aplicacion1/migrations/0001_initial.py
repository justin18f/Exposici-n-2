# Generated by Django 4.1.1 on 2022-09-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Nacimiento', models.CharField(max_length=50)),
                ('Enfermedad', models.CharField(max_length=50)),
                ('Tratamiento', models.CharField(max_length=200)),
            ],
        ),
    ]
