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
        # set url
        self.browser.get(self.live_server_url + "/")
        # get module select
        elem = self.browser.find_element_by_id('searchTextarea')
        elem.send_keys("nutella")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertEqual(self.browser.current_url, self.live_server_url + "/food/result/")



    """def test_project_info_form(self):
        # set url
        self.browser.get(self.live_server_url + '/')
        # get module select
        self.browser.find_element_by_id('userLogoLi').click()
        test = self.browser.find_element_by_xpath(
            "//label[@id='mail']"
        ).click()
        test.send_keys("test")"""
