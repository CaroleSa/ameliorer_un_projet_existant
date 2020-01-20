#! /usr/bin/env python3
# coding: UTF-8

""" TestCallApi class """


# imports
from unittest import TestCase
from unittest.mock import patch
from food.classes.call_api import CallApi


class TestCallApi(TestCase):
    """ TestCallApi class :
    test_return_request method """

    def setUp(self):
        self.new_call_api = CallApi()

    @patch('food.classes.call_api.requests.get')
    def test_return_request(self, mock_api):
        """ Verify that the method returns the data """

        result_json = {'count': 0, 'page_size': '100', 'products': [], 'page': '1', 'skip': 0}, \
                      {'skip': 0, 'page': 1, 'products': [], 'page_size': 100, 'count': 0}, \
                      {'skip': 0, 'page': '1', 'products': [], 'page_size': '100', 'count': 0}, \
                      {'page': '1', 'skip': 0, 'count': 0, 'page_size': '100', 'products': []}, \
                      {'skip': 0, 'page': '1', 'page_size': '100', 'products': [], 'count': 10}
        mock_api.return_value.json.return_value = result_json
        result_list = [result_json]

        categories_list = ["pizza"]

        self.assertEqual(self.new_call_api.load_data(categories_list), result_list)
