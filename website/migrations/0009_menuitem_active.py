# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20161112_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]