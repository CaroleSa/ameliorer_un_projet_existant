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
    method test_search_food """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_search_food(self):
        """ test the functionality of the user food searches """
        # set url
        self.browser.get(self.live_server_url + "/")

        # test search nutella in textarea (at the top of the page)
        search_textarea = self.browser.find_element_by_id("searchTextarea")
        name_food = "nutella"
        search_textarea.send_keys(name_food)
        search_textarea.send_keys(Keys.RETURN)
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check the value of the title of the result page
        title = self.browser.find_element_by_id("titleFoodSearched").text
        self.assertEqual(title, "Aliment recherché : " + name_food)
        # check that the result display
        name_food = self.browser.find_element_by_id("nameFood").text
        self.assertNotEqual(name_food, "")

        # test click on the food image of the result page
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        food_image = self.browser.find_element_by_id("image")
        food_image.click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/detail/")

        # test that the detailed food (detail page) is the same as the food clicked
        # in the result page
        name_food_detail_page = self.browser.find_element_by_id("nameFoodDetail").text
        self.assertEqual(name_food_result_page, name_food_detail_page)

        # test click to the OpenFoodFacts link
        link = self.browser.find_element_by_id("link")
        value_link = link.get_attribute("href")
        link.click()
        # check the OpenFoodFacts link value
        self.assertRegex(value_link, "^https://fr.openfoodfacts.org/produit/[0-9]*/[a-z-]*")

        # test search pizza in textarea (at the middle of the page)
        self.browser.find_element_by_id("exitLogoLi").click()
        time.sleep(5)
        self.browser.find_element_by_id("productTextarea").send_keys("pizza")
        self.browser.find_element_by_id("button_search").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")

        # test click to the save logo
        self.browser.find_element_by_id("floppy").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/access_account/")

        # test click to the exit logo
        self.browser.find_element_by_id("exitLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")

        # test a search without result in textarea
        food_name = "salade"
        self.browser.find_element_by_id("productTextarea").send_keys(food_name)
        self.browser.find_element_by_id("button_search").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Pas de résultat pour l'aliment " + food_name + ".")
