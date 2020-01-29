#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
from unittest import TestCase
from selenium import webdriver


class TestUserTakesTheTest(TestCase):
    """ geckodriver and firefox
    must be in your path """

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_results_page_shows(self):
        self.driver.get("http://206.189.30.225/")

    def tearDown(self):
        self.driver.close()