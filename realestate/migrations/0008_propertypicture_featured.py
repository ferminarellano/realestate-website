# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0007_propertypicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertypicture',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='Featured'),
        ),
    ]
