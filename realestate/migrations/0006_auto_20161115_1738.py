# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 17:38
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_auto_20161114_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, upload_to='properties/main', verbose_name='Picture'),
        ),
    ]
