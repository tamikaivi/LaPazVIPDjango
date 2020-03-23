# Generated by Django 3.0.4 on 2020-03-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField()),
                ('contacto', models.IntegerField()),
                ('zona', models.TextField()),
                ('precio', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
    ]
