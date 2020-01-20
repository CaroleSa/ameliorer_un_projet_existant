#! /usr/bin/env python3
# coding: UTF-8

""" TestDatabase class """


# imports
from unittest import TestCase
from food.models import Food, Categorie


class TestDatabase(TestCase):
    """ TestDatabase class :
    test_food_data_exists method
    test_categorie_data_exists method
    test_food_name_exists method
    test_categorie_name_exists method """

    def setUp(self):
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

    def test_categorie_data_exists(self):
        """ Verify that the database contains the categorie data """
        self.assertTrue(Categorie.objects.all().exists())

    def test_food_data_exists(self):
        """ Verify that the database contains the food data """
        self.assertTrue(Food.objects.all().exists())

    def test_food_name_exists(self):
        """ Verify that the Food table contains the name : name_test """
        try:
            Food.objects.get(name="name_test")
            name = True
        except Food.DoesNotExist:
            name = False
        self.assertTrue(name)

    def test_categorie_name_exists(self):
        """ Verify that the Categorie table contains the name : name_test """
        try:
            Categorie.objects.get(name="name_test")
            name = True
        except Categorie.DoesNotExist:
            name = False
        self.assertTrue(name)
