#! /usr/bin/env python3
# coding: UTF-8

""" TestUserTakesTheTest class """

# imports
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from food.models import Food


class TestUserTakesTheTest(StaticLiveServerTestCase):
    """ class TestUserTakesTheTest :
    test user actions regarding their account """

    def setUp(self):
        self.browser = webdriver.Firefox()

        # CREATE USER ACCOUNT 1
        self.user = get_user_model()
        self.dict_data_access_account = {"mail": "carole1@test.fr", "password": "00000000"}
        self.user_created = \
            self.user.objects.create_user(username='Null',
                                          email=self.dict_data_access_account.get('mail'),
                                          password=self.dict_data_access_account.get('password'))

        # DATA TO CREATE USER ACCOUNT 2
        self.mail_create_account = "carole2@test.fr"
        self.dict_data_create_account = {"mail": self.mail_create_account,
                                         "password": self.dict_data_access_account.get('password'),
                                         "password2": self.dict_data_access_account.get('password')}

    def tearDown(self):
        self.browser.quit()

    def test_access_favorites_logout(self):
        """ test access to favorites page if the user is not connected """
        self.browser.get(self.live_server_url + "/account/access_account/")
        self.browser.find_element_by_id("carrotLogoLi").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Veuillez vous connecter pour accéder à vos favoris.")

    def test_login_error(self):
        """ connection test with an unknown email """
        self.browser.get(self.live_server_url + "/food/favorites/")
        self.browser.find_element_by_id("userLogoLi").click()
        dict_data_account_unknown = {"mail": "unknown_email@test.fr", "password": "00000000"}
        for key, value in dict_data_account_unknown.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/access_account/")
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Ce compte n'existe pas.")

    def test_create_account(self):
        """ test create user account """
        self.browser.get(self.live_server_url + "/account/access_account/")
        self.browser.find_element_by_id("buttonCreateAccount").click()
        for key, value in self.dict_data_create_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submitButton").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/create_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message,
                         "Le compte " + self.mail_create_account + " a bien été créé.")

    def test_login(self):
        """ test user login """
        self.browser.get(self.live_server_url + "/account/create_account/")
        self.browser.find_element_by_id("userLogoLi").click()
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url,
                         self.live_server_url + "/account/access_account/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message,
                         "Bonjour " + self.dict_data_access_account.get('mail')
                         + " ! Vous êtes bien connecté.")

    def test_access_favorite_page_login(self):
        """ test access to favorites page if the user is logged """
        self.test_login()
        self.browser.find_element_by_id("carrotLogoLi").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check the title of the favorites page
        title = self.browser.find_element_by_id("favoritesTitle").text
        self.assertEqual(title, "Mes aliments")

    def save_favorite_food(self):
        """ test save favorite food """
        self.test_login()
        search_textarea = self.browser.find_element_by_id("searchTextarea")
        search_textarea.send_keys("nutella")
        search_textarea.send_keys(Keys.RETURN)
        name_food_result_page = self.browser.find_element_by_id("nameFood").text
        self.browser.find_element_by_id("floppy").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")
        # check that the selected food is present in the favorites page
        self.browser.find_element_by_id("carrotLogoLi").click()
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertEqual(name_favorite_food, name_food_result_page)

    def delete_favorite_food(self):
        """ test delete favorite food """
        self.test_login()
        food = Food.objects.get(id=1)
        user = self.user.objects.get(id=1)
        food.favorites.add(user)
        self.browser.find_element_by_id("carrotLogoLi").click()
        self.browser.find_element_by_class_name("delete").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/favorites/")
        # check that the deleted favorite food is not present in the favorites page
        name_favorite_food = self.browser.find_element_by_id("nameFood").text
        self.assertEqual(name_favorite_food, "")

    def test_user_disconnection(self):
        """ test user disconnection if he clicked to the exit logo """
        self.test_login()
        self.browser.find_element_by_id("exitLogoLi").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Vous êtes déconnecté.")

    def test_access_my_account_page(self):
        """ test access to my account page """
        self.test_login()
        self.browser.find_element_by_id("userLogoLi").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/account/my_account/")
        # check the value of the title of the my account page
        title = self.browser.find_element_by_id("titleMyAccount").text
        self.assertEqual(title, "Mes informations :")
        # check that the email of the my account page is the same that connection email
        mail_account = self.browser.find_element_by_id("mailAccount").text
        self.assertEqual(mail_account, "Votre adresse e-mail : "
                         + self.dict_data_access_account.get('mail'))

    def test_delete_account(self):
        """ test delete user account """
        self.test_login()
        self.browser.find_element_by_id("userLogoLi").click()
        self.browser.find_element_by_id("deleteAccount").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url + "/")
        # check the value of the confirmation message
        confirmation_message = self.browser.find_element_by_id("confirmationMessage").text
        self.assertEqual(confirmation_message, "Votre compte a bien été supprimé.")

    def test_login_account_deleted(self):
        """ test login with account deleted """
        self.user = self.user_created
        self.user.is_active = False
        self.user.save()
        self.browser.get(self.live_server_url + "/account/access_account/")
        for key, value in self.dict_data_access_account.items():
            self.browser.find_element_by_id(key).send_keys(value)
        self.browser.find_element_by_id("submit").click()

        # check the url of the recovered page
        self.assertEqual(self.browser.current_url, self.live_server_url
                         + "/account/access_account/")
        # check the value of the error message
        error_message = self.browser.find_element_by_id("red").text
        self.assertEqual(error_message, "Ce compte n'existe plus.")
