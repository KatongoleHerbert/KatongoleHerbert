# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180319_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='std_id',
            field=models.CharField(max_length=14, unique=True, verbose_name='Student ID'),
        ),
    ]
