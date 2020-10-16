import time
import unittest
import traceback
import sys
import os
import time
import namasteFit.CommonFiles.excelUtils as XUtils
import gspread
from oauth2client.service_account import ServiceAccountCredentials

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
import namasteFit.CommonFiles.googleSheetsUtils as sheetsUtils
from namasteFit.TestServer.Pages.landingPage import LandingPage
from namasteFit.TestServer.Pages.mysitePage import MySitePage
from namasteFit.TestServer.Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TestResults = ""
drivers = []
user_story = "107"


class LoginUnitTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        drivers.append({"webdriver": webdriver.Firefox, "executable_path": Locators.firefox_driver})
        drivers.append({"webdriver": webdriver.Chrome, "executable_path": Locators.chrome_driver})
        drivers.append({"webdriver": webdriver.Edge, "executable_path": Locators.microsoft_edge_driver})
        # return cls.driver

    def test_login(self):
        for browser in drivers:
            self.driver = browser["webdriver"](executable_path=browser["executable_path"])
            self.driver.get(Locators.testServer + Locators.login_url)
            self.driver.maximize_window()
            driver = self.driver
            driver.set_script_timeout(60)
            namaste_username = Locators.namaste_username
            namaste_password = Locators.namaste_password

            email_field_id = Locators.email_field_id
            pass_field_id = Locators.pass_field_id
            login_button_xpath = Locators.login_button_xpath
            namaste_logo_xpath = Locators.namaste_logo_xpath

            email_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_field_id)))
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
            driver.refresh()

            # print(url)
            time.sleep(3)
            try:
                self.assertEqual(url, driver.current_url, "The page should return to " + url)
                TestResults = "PASS"
                # sheetsUtils.write_results(TestResults, browser["executable_path"], user_story)

            except Exception:
                TestResults = "FAIL"
                # sheetsUtils.write_results(TestResults, browser["executable_path"], user_story)

            driver.close()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()


if __name__ == '__main_':
    unittest.main()
