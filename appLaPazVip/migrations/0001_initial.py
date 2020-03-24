# Generated by Django 3.0.4 on 2020-03-23 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('ciudad', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Duenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('direccion', models.TextField()),
            ],
        ),
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
                ('duenio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appLaPazVip.Duenio')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appLaPazVip.Cliente')),
                ('servicio', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appLaPazVip.Servicio')),
            ],
        ),
    ]
