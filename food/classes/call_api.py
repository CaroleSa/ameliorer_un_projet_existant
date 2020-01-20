#! /usr/bin/env python3
# coding: UTF-8

""" CallApi class """


# import
import requests


class CallApi:
    """ Call A.P.I. OpenFoodFacts :
    load_data method """

    def __init__(self):
        # creating an empty list
        self.list_data = []

    def load_data(self, categories):
        """ Adds a categories food list
        and returns a data list of the A.P.I. Open Food Facts,
        convert to json """

        for elt in categories:
            payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
                       'tag_0': "\'" + elt + "\'", 'sort_by': 'unique_scans_n', 'page_size': 100,
                       'axis_x': 'energy', 'axis_y': 'products_n', 'json': '1'}
            request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
            data = request.json()
            self.list_data.append(data)

        return self.list_data
