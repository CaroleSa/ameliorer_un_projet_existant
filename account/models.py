#! /usr/bin/env python3
# coding: UTF-8

""" Custom User model """


# Imports
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _
import django


class User(AbstractUser):
    """ Custom User Model """
    USERNAME_FIELD = 'email'
    # edit email and username fields of the User model
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), null=True, max_length=150,
                                validators=[django.contrib.auth.validators.
                                            UnicodeUsernameValidator()])
    REQUIRED_FIELDS = ['username']
