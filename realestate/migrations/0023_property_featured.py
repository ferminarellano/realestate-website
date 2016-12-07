# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0022_property_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='Featured Property'),
        ),
    ]