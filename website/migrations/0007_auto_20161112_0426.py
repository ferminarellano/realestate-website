# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20161111_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.PositiveIntegerField(unique=True, verbose_name='Position'),
        ),
    ]
