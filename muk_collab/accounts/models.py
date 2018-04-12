# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, std_id, password=None):
        """
        Creates and saves a User with the given username, phone number and password.
        """
        if not std_id:
            raise ValueError('Users must have a username')

        user = self.model(
            std_id=std_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, std_id, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            std_id=std_id,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = None
    std_id = models.CharField(_('Student ID'), max_length=14, unique=True)
    course = models.CharField(max_length=30, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def get_full_name(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)

    USERNAME_FIELD = 'std_id'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = "Users"
