#! /usr/bin/env python3
# coding: UTF-8

""" Models """


# Imports
from django.db import models
from django.contrib.auth import get_user_model


class Categorie(models.Model):
    """ Categorie model
    field : name """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    """ Food model
    fields : name, categorie, nutrition_grade, url_picture,
    link, energy, proteins, fat, carbohydrates, sugars,
    fiber, sodium, favorites """
    User = get_user_model()
    name = models.CharField(max_length=120, unique=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nutrition_grade = models.CharField(max_length=1)
    url_picture = models.URLField(unique=True)
    link = models.URLField(unique=True)
    energy = models.CharField(max_length=10, null=True)
    proteins = models.CharField(max_length=10, null=True)
    fat = models.CharField(max_length=10, null=True)
    carbohydrates = models.CharField(max_length=10, null=True)
    sugars = models.CharField(max_length=10, null=True)
    fiber = models.CharField(max_length=10, null=True)
    sodium = models.CharField(max_length=10, null=True)
    favorites = models.ManyToManyField(User)

    def __str__(self):
        return self.name, self.categorie, self.nutrition_grade, self.url_picture, self.link, \
               self.energy, self.proteins, self.fat, self.carbohydrates, self.sugars, self.fiber, \
               self.sodium
