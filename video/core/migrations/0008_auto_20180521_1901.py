# Generated by Django 2.0.5 on 2018-05-21 19:01

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180521_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_uploaded',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.date(2017, 5, 21))]),
        ),
        migrations.AlterField(
            model_name='video',
            name='points',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]