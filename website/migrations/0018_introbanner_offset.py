# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20161118_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='introbanner',
            name='offset',
            field=models.IntegerField(blank=True, null=True, verbose_name='Offset'),
        ),
    ]
