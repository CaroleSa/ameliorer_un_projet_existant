#! /usr/bin/env python3
# coding: UTF-8

""" Context processor """


# import
from django.conf import settings


def menu(request):
    """ add the authenticated status
    in all the contexts """
    if request.user.is_authenticated:
        return {'authenticated': 'True'}

    return {'authenticated': 'False'}
