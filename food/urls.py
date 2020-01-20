#! /usr/bin/env python3
# coding: UTF-8

""" Food URLS """


# imports
from django.conf.urls import url
from . import views


app_name = 'food'

urlpatterns = [
    url(r'^result/$', views.result, name="result"),
    url(r'^detail/$', views.detail, name="detail"),
    url(r'^favorites/$', views.favorites, name="favorites")
]
