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

TestResults = ""
drivers = []
user_story = "107"

#Get Started
class Phoenix_07(unittest.TestCase):
    def setUp(self):
        drivers.append({"webdriver": webdriver.Firefox, "executable_path": Locators.firefox_driver})
        drivers.append({"webdriver": webdriver.Chrome, "executable_path": Locators.chrome_driver})
        drivers.append({"webdriver": webdriver.Edge, "executable_path": Locators.microsoft_edge_driver})

    def test_107(self):
        for browser in drivers:
            self.driver = browser["webdriver"](executable_path=browser["executable_path"])
            self.driver.get(Locators.testServer + Locators.login_url)
            self.driver.maximize_window()
            driver = self.driver

            # Login email_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_field_id)))
            namaste_username = Locators.namaste_username
            namaste_password = Locators.namaste_password
            email_field_id = Locators.email_field_id
            pass_field_id = Locators.pass_field_id
            login_button_xpath = Locators.login_button_xpath
            namaste_logo_xpath = Locators.namaste_logo_xpath

            email_field_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, email_field_id)))
            pass_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, pass_field_id)))
            login_button_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, login_button_xpath)))

            email_field_element.clear()
            email_field_element.send_keys(namaste_username)

            pass_field_element.clear()
            pass_field_element.send_keys(namaste_password)

            login_button_element.click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, namaste_logo_xpath)))

        # def test_page_refresh(self):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
            url = driver.current_url
            # driver.refresh()

        # test PHOENIX -7
            time.sleep(5)
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