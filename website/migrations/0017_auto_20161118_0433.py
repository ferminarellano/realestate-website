# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_introbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='introbanner',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='introbanner',
            name='caption_description_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption Description'),
        ),
        migrations.AddField(
            model_name='introbanner',
            name='caption_description_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption Description'),
        ),
        migrations.AddField(
            model_name='introbanner',
            name='caption_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption Title'),
        ),
        migrations.AddField(
            model_name='introbanner',
            name='caption_title_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Caption Title'),
        ),
        migrations.AddField(
            model_name='introbanner',
            name='position',
            field=models.PositiveIntegerField(default=1, unique=True, verbose_name='Position'),
            preserve_default=False,
        ),
    ]
