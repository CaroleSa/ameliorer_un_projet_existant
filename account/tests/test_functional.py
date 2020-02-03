#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestUserTakesTheTest(StaticLiveServerTestCase):
    """ class TestUserTakesTheTest
    method test_user_account """

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        self.dict_data_access_account = {"mail": "carole@test.fr", "password": "00000000"}
        self.dict_data_create_account = {"mail": "carole@test.fr", "password": "00000000",
                                         "password2": "00000000"}
        self.mail_connection = self.dict_data_access_account.get("mail")

    def tearDown(self):
        self.browser.quit()

    def test_user_account(self):
        """ test the functionality of the user account """
        # set url
        self.browser.get(self.live_server_url + "/")

        # test access favorites if the user is not logged
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Veuillez vous connecter pour accéder à vos favoris.")

        # test click to the account logo
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/access_account/")

        # connection test with an unknown email
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Ce compte n'existe pas.")

        # test of the creation of the user account
        self.browser.find_element_by_id("buttonCreateAccount").click()
        for key, value in self.dict_data_create_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submitButton").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/create_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message,
                         "Le compte " + self.mail_connection + " a bien été créé.")

        # test of connection with created user
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/access_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message,
                         "Bonjour " + self.mail_connection + " ! Vous êtes bien connecté.")

        # test access favorites if the user is logged
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the title of the favorites page
        title = self.browser.find_element_by_id("favoritesTitle").text
        self.assertEqual(title, "Mes aliments")

        # test add favorite food
        search_textarea = self.browser.find_element_by_id("searchTextarea")
        search_textarea.send_keys("nutella")
        search_textarea.send_keys(Keys.RETURN)
        time.sleep(5)
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        self.browser.find_element_by_id("floppy").click()
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check that the selected food is present in the favorites page
        self.browser.find_element_by_id("carrotLogoLi").click()
        time.sleep(5)
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertEqual(name_favorite_food, name_food_result_page)

        # test delete favorite
        self.browser.find_element_by_class_name("delete").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check that the deleted favorite food is not present in the favorites page
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertEqual(name_favorite_food, "")

        # test user disconnection
        self.browser.find_element_by_id("exitLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Vous êtes déconnecté.")

        # test access to my account page
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/my_account/")
        # check the value of the title of the my account page
        title = self.browser.find_element_by_id("titleMyAccount").text
        self.assertEqual(title, "Mes informations :")
        # check that the email of the my account page is the same that connection email
        mail_account = self.browser.find_element_by_id("mailAccount").text
        self.assertEqual(mail_account, "Votre adresse e-mail : " + self.mail_connection)

        # test delete user account
        self.browser.find_element_by_id("deleteAccount").click()
        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Votre compte a bien été supprimé.")

        # test of connection with the user account deleted
        self.browser.find_element_by_id("userLogoLi").click()
        time.sleep(5)
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()
        time.sleep(5)
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Ce compte n'existe plus.")
