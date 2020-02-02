#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class TestUserTakesTheTest(StaticLiveServerTestCase):
    """ geckodriver and firefox
    must be in your path """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_access_result_page(self):
        # AJOUTE TEST CONTENU DE LA PAGE PUIS SI CLIQUE SUR IMAGE OU SAVEGARDE
        # set url
        self.browser.get(self.live_server_url + "/")
        # get module select
        elem = self.browser.find_element_by_id("searchTextarea")
        elem.send_keys("nutella")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # tester le contenu de la page

        self.browser.find_element_by_id("image").click()
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/detail/")
        # tester le contenu de la page
        # tester le click sur l'enregistrement et voir si enregistré dans favoris
        # tester le click page suivante

        """# test clique sur lien openfoodfacts
        self.browser.find_element_by_id("link").click()
        time.sleep(15)
        print("test eeeeeeeeee", self.browser.current_url)
        # curret url ne donne pas le site openfood facts mais le site page detail
        self.assertRegex(self.browser.current_url, r"^https://fr.openfoodfacts.org/produit/[0-9]*/[a-z-_]*&")"""

        # set url
        self.browser.get(self.live_server_url + "/")
        # get module select
        self.browser.find_element_by_id("productTextarea").send_keys("pizza")
        self.browser.find_element_by_id("button_search").click()
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")

        # test click sur logo accueil

    """def test_access_access_account_page(self):
        # AJOUTE TEST CONTENU DE LA PAGE
        # set url
        self.browser.get(self.live_server_url + "/")
        # get module select
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")"""
