# Generated by Django 2.2.3 on 2019-07-04 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0015_auto_20190704_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2019, 7, 4, 17, 54, 57, 211387)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nac',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 4, 17, 54, 57, 210389)),
        ),
    ]