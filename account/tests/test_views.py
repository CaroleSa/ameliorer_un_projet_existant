#! /usr/bin/env python3
# coding: UTF-8

""" TestViews class """


# imports
from unittest import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """ TestViews class :
    test_add_user method
    """

    def setUp(self):
        self.user = get_user_model()
        self.email = 'test@test2.com'
        self.password = 'testtest'
        self.id_user = 2

    def test_add_user(self):
        # add user
        try:
            self.user.objects.get(email=self.email).delete()
        except self.user.DoesNotExist:
            pass
        self.user.objects.create_user(id=self.id_user, username='Null', email=self.email, password=self.password)

        # try to get the data from an existing user (id = 2)
        # and from an nonexistent user (id = 5)
        dict = {self.id_user: self.assertTrue, '5': self.assertFalse}
        for key, value in dict.items():
            try:
                self.user.objects.get(id=key)
                data = True
            except self.user.DoesNotExist:
                data = False
            value(data)
