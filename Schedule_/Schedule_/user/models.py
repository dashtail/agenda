# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    name = models.CharField(
        verbose_name=u"Nome",
        blank=False,
        null=True,
        max_length=50
        )

    def get_absolute_url(self):
        return '/Usuarios/'

    class Meta:
        db_table  = "user_profile"
