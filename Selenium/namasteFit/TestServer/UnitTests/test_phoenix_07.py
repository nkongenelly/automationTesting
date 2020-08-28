import time
import unittest
import traceback
import sys
import os
import time
import namasteFit.CommonFiles.excelUtils as XUtils
import gspread
import namasteFit.CommonFiles.googleSheetsUtils as sheetsUtils
from oauth2client.service_account import ServiceAccountCredentials
from namasteFit.TestServer.Pages.landingPage import LandingPage
from namasteFit.TestServer.UnitTests.test_valid_login import LoginTest
from namasteFit.TestServer.Pages.mysitePage import MySitePage
from namasteFit.TestServer.Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class Phoenix_07(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=Locators.firefox_driver)
        self.driver.get(Locators.testServer + Locators.login_url)
        self.driver.maximize_window()

    def test_107(self):
        LoginTest.test_login(self)
        driver = self.driver
        get_started_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
        customize_site_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.customize_my_site_button_xpath)))
        setup_events_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.setup_events_button_xpath)))
        my_site_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.mysite_button_id)))
        my_events_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.my_events_button_id)))
        members_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.members_button_id)))
        if get_started_element == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.get_started_text_text)

        if customize_site_button == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.customize_my_site_button_text)

        if setup_events_button == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.setup_events_button_text)

        if my_site_button == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.mysite_button_id)

        if my_events_button == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.my_events_button_text)

        if members_button == "null":
            element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
            assert element.text(Locators.my_events_button_text)


    def tearDown(self) -> None:
        self.driver.close()