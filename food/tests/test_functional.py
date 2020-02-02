#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class TestUserTakesTheTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_search_food(self):
        # set url
        self.browser.get(self.live_server_url + "/")

        # test search nutella in textarea (at the top of the page)
        elem = self.browser.find_element_by_id("searchTextarea")
        elem.send_keys("nutella")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")

        # test click on the food image of the result page
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        elem = self.browser.find_element_by_id("image")
        elem.click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/detail/")

        # test that the detailed food (detail page) is the same as the food clicked in the result page
        name_food_detail_page = self.browser.find_element_by_id("nameFoodDetail").text
        self.assertEqual(name_food_result_page, name_food_detail_page)
        # tester le click sur l'enregistrement et voir si enregistré dans favoris

        # test click to the OpenFoodFacts link
        elem = self.browser.find_element_by_id("link")
        link = elem.get_attribute("href")
        elem.click()
        # check the OpenFoodFacts link value
        self.assertRegex(link, "^https://fr.openfoodfacts.org/produit/[0-9]*/[a-z-]*")

        # set url
        self.browser.get(self.live_server_url + "/")
        # test search pizza in textarea (at the middle of the page)
        self.browser.find_element_by_id("productTextarea").send_keys("pizza")
        self.browser.find_element_by_id("button_search").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")

        # test click to the save logo
        self.browser.find_element_by_id("floppy").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")

        # test click to the exit logo
        self.browser.find_element_by_id("exitLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
