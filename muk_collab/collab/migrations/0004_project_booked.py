# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-02 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0003_remove_project_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='booked',
            field=models.BooleanField(default=True),
        ),
    ]