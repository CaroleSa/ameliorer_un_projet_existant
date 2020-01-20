#! /usr/bin/env python3
# coding: UTF-8

""" TestViews class """


# imports
from unittest import TestCase
from food.models import Food, Categorie
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """ TestViews class :
    test_add_favorites method
    test_delete_favorites method
    """

    def setUp(self):
        # create an user
        self.user = get_user_model()
        self.user_email = "test@test1.fr"
        try:
            self.user.objects.get(email=self.user_email).delete()
        except self.user.DoesNotExist:
            pass
        self.id_user = 1
        self.user.objects.create_user(id=self.id_user, username='Null', email=self.user_email, password='testtest')

        # create an food
        try:
            Categorie.objects.get(name="name_test").delete()
        except Categorie.DoesNotExist:
            pass
        try:
            Food.objects.get(name="name_test").delete()
        except Food.DoesNotExist:
            pass
        Categorie.objects.create(name="name_test")
        categorie_id = Categorie.objects.get(name="name_test")
        Food.objects.create(name="name_test", categorie=categorie_id,
                            nutrition_grade="A", url_picture="url_test",
                            link="link_test", energy="100",
                            proteins="100", fat="100",
                            carbohydrates="100",
                            sugars="100", fiber="100",
                            sodium="100")
        self.id_food = 1

    def test_add_favorites(self):
        # add favorites
        food = Food.objects.get(name="name_test")
        user = self.user.objects.get(id=self.id_user)
        food.favorites.add(user)

        # try to get the favorites data
        try:
            self.user(id=self.id_user).food_set.get(name="name_test")
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertTrue(data)

        try:
            self.user(id=self.id_user).food_set.get(id=2)
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertFalse(data)

    def test_delete_favorites(self):
        # delete favorites
        food = Food.objects.get(name="name_test")
        user = self.user.objects.get(id=self.id_user)
        food.favorites.remove(user)

        # try to get the favorites data
        try:
            self.user(id=self.id_user).food_set.get(id=self.id_user)
            data = True
        except Food.DoesNotExist:
            data = False
        self.assertFalse(data)
