#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestUserTakesTheTest(StaticLiveServerTestCase):
    """ class TestUserTakesTheTest :
    test the user's food search """

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_search_middle_textarea(self):
        """ test search pizza in textarea (in the middle of the page)
        and display result and detail pages """
        self.browser.get(self.live_server_url + "/")
        self.browser.find_element_by_id("productTextarea").send_keys("pizza")
        self.browser.find_element_by_id("button_search").click()
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check that the result display
        name_food = self.browser.find_element_by_id("nameFood").text
        self.assertNotEqual(name_food, "")

        # TEST DISPLAY THE FOOD DETAIL
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        self.browser.find_element_by_id("image").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/detail/")
        # test that the detailed food (detail page) is the same as the food clicked
        # in the result page
        name_food_detail_page = self.browser.find_element_by_id("nameFoodDetail").text
        self.assertEqual(name_food_result_page, name_food_detail_page)

        # TEST CLICK TO THE OPENFOODFACTS LINK
        link = self.browser.find_element_by_id("link")
        value_link = link.get_attribute("href")
        link.click()
        time.sleep(5)
        # check the OpenFoodFacts link value
        self.assertRegex(value_link, "^https://fr.openfoodfacts.org/produit/[0-9]*/[a-z-]*")

    def test_error_result(self):
        """ test a search without result in textarea (at the top of the page) """
        self.browser.get(self.live_server_url + "/account/create_account/")
        food_name = "salade"
        textarea = self.browser.find_element_by_id("searchTextarea")
        textarea.send_keys(food_name)
        textarea.send_keys(Keys.RETURN)
        time.sleep(5)

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Pas de résultat pour l'aliment " + food_name + ".")
