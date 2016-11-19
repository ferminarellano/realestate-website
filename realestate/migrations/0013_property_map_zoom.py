# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0012_auto_20161119_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='map_zoom',
            field=models.PositiveIntegerField(default=16, verbose_name='Map Zoom'),
        ),
    ]