#! /usr/bin/env python3
# coding: UTF-8

""" Account URLS """


# imports
from django.conf.urls import url
from . import views


app_name = 'account'

urlpatterns = [
    url(r'^access_account/$', views.access_account, name="access_account"),
    url(r'^create_account/$', views.create_account, name="create_account"),
    url(r'^my_account/$', views.my_account, name="my_account")
]
