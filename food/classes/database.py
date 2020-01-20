#! /usr/bin/env python3
# coding: UTF-8

""" Database class """


# imports
from django.db.utils import IntegrityError
from food.models import Food, Categorie
from food.classes.call_api import CallApi


class Database:
    """ Database class :
    insert_data method """

    def __init__(self):
        # instantiate the Call_api class
        self.new_call_api = CallApi()

    def insert_data(self):
        """ call load_data method of the CallApi class,
        get a list of data of the OpenFoodFacts A.P.I.
        and insert the data in the database :
        if the database is empty """

        # INSERT DATA IN THE DATABASE
        # if the database is empty
        data_food = Food.objects.all()
        if not data_food:

            # get the data food of the CallApi class
            categories_food = ['pizza', 'pate a tartiner', 'gateau', 'yaourt', 'bonbon']
            list_data = self.new_call_api.load_data(categories_food)

            # INSERT DATA
            for elt, data in zip(categories_food, list_data):
                # insert data in Categorie table
                index = categories_food.index(elt) + 1
                Categorie.objects.create(name=elt)

                for value in data['products']:
                    if data['products'].index(value) < 100:
                        try:
                            # get data product_name, nutrition_grade, ...
                            product_name = value['product_name_fr']
                            grade = value['nutrition_grade_fr']
                            picture = value['image_url']
                            page_link = value['url']
                            nutriments = value['nutriments']
                            energy_100g = nutriments.get('energy_100g')
                            proteins_100g = nutriments.get('proteins_100g')
                            fat_100g = nutriments.get('fat_100g')
                            carbohydrates_100g = nutriments.get('carbohydrates_100g')
                            sugars_100g = nutriments.get('sugars_100g')
                            fiber_100g = nutriments.get('fiber_100g')
                            sodium_100g = nutriments.get('sodium_100g')

                            # insert data in Food table
                            categorie_id = Categorie.objects.get(id=index)
                            Food.objects.create(name=product_name, categorie=categorie_id,
                                                nutrition_grade=grade, url_picture=picture,
                                                link=page_link, energy=energy_100g,
                                                proteins=proteins_100g, fat=fat_100g,
                                                carbohydrates=carbohydrates_100g,
                                                sugars=sugars_100g, fiber=fiber_100g,
                                                sodium=sodium_100g)

                        except IntegrityError:
                            continue
                        except KeyError:
                            continue
