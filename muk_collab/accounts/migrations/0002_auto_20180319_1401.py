# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='System_user',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
