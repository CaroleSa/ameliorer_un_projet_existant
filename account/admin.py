#! /usr/bin/env python3
# coding: UTF-8

""" Account admin """

# imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
