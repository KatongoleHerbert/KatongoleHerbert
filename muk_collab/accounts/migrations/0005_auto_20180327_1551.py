# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]