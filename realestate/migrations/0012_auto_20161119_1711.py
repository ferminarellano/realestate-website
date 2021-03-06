# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0011_remove_property_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.FloatField(default=1, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.FloatField(default=1, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]
