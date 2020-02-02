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

    """def tearDown(self):
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
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")"""



    """def test_access_access_account_page(self):
        # AJOUTE TEST CONTENU DE LA PAGE
        # set url
        self.browser.get(self.live_server_url + "/")
        # get module select
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")
        search_form = driver.find_element_by_tag_name("form")"""
