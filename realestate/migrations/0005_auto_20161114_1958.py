# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0004_property_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_es',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='country',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description_es',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name_es',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=models.CharField(max_length=255, verbose_name='Neighborhood'),
        ),
        migrations.AlterField(
            model_name='property',
            name='picture',
            field=stdimage.models.StdImageField(blank=True, upload_to='properties/main', verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='State'),
        ),
    ]