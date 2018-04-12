# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from accounts.models import User


class Project(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)
    booked = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()


class eval_table(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{:%H:%M},{:%H:%M}'.format(self.start_time, self.end_time)


class Results(models.Model):
    project = models.ForeignKey(Project)
    final_result = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Results'


class My_workables(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '{:%H:%M},{:%H:%M}'.format(self.start_time, self.end_time)




