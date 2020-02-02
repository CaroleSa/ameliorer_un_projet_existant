#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class TestUserTakesTheTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_user_account(self):
        # set url
        self.browser.get(self.live_server_url + "/")

        # test access favorites if no connected
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Veuillez vous connecter pour accéder à vos favoris.")

        # test click to account logo
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")

        # test access account with a mail unknown
        self.browser.find_element_by_id("mail").send_keys("carole@test.fr")
        self.browser.find_element_by_id("password").send_keys("00000000")
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Ce compte n'existe pas.")

        # test create account
        self.browser.find_element_by_id("buttonCreateAccount").click()
        self.browser.find_element_by_id("mail").send_keys("carole@test.fr")
        self.browser.find_element_by_id("password").send_keys("00000000")
        self.browser.find_element_by_id("password2").send_keys("00000000")
        self.browser.find_element_by_id("submitButton").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/create_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Le compte carole@test.fr a bien été créé.")

        # test access account with the account created
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        self.browser.find_element_by_id("mail").send_keys("carole@test.fr")
        self.browser.find_element_by_id("password").send_keys("00000000")
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Bonjour carole@test.fr ! Vous êtes bien connecté.")

        # test access favorites if connected
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the title of the favorites page
        title = self.browser.find_element_by_id("favoritesTitle").text
        self.assertEqual(title, "Mes aliments")

        # test add favorites food
        elem = self.browser.find_element_by_id("searchTextarea")
        elem.send_keys("nutella")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        self.browser.find_element_by_id("floppy").click()
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")
        # check the favorite food is registered
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertEqual(name_favorite_food, name_food_result_page)

        # test delete favorite
        self.browser.find_element_by_id("delete").click()
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/access_account/")
        # check the favorite food is deleted
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertIsNone(name_favorite_food)




        #test suprime et test deconnexion, test suprimer compte et essayer de se reconnecter




