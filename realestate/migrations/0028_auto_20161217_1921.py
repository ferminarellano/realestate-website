# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0027_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug_en',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='slug_es',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
