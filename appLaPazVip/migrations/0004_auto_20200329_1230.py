# Generated by Django 3.0.4 on 2020-03-29 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLaPazVip', '0003_auto_20200329_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
