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

class LoginUnitTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=Locators.firefox_driver)
        cls.driver.get(Locators.testServer + Locators.login_url)
        cls.driver.maximize_window()
        return cls.driver

    def test_login(self):
        driver = self.driver
        driver.set_script_timeout(60)
        namaste_username = "nelly@namaste.fit"
        namaste_password = "qwertyui"

        email_field_id = "form-signin-email"
        pass_field_id = "form-signin-password"
        login_button_xpath = "//*[@id='formLogin']/button"
        namaste_logo_xpath = "//*[@id='mainLogo']"

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

    def test_page_refresh(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
        url = self.driver.current_url
        self.driver.refresh()

        # print(url)
        time.sleep(3)
        try:
            print(url)
            print(self.driver.current_url)
            self.assertEqual(url, self.driver.current_url, "The page should return to " + url)
            TestResults = "PASS"
            print("1")
            print(TestResults)
            write_results(TestResults)

        except Exception:
            # var = traceback.format_exc()
            # print(var)
            TestResults = "FAIL"
            print("2")
            print(TestResults)
            write_results(TestResults)

        # assertion = self.assertTrue(url, self.driver.current_url, "The page should return to " + url)
        # print(assertion)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


def write_results(TestResults):
    written = False
    print("3")
    print(TestResults)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(Locators.credentials, Locators.scope)
    client = gspread.authorize(credentials)
    max_rows = sheetsUtils.getRowCount(Locators.userStoriesTestCases, client)

    print(max_rows)
    for row in range(max_rows + 1):
        print(row)
        row_value = sheetsUtils.readData(Locators.userStoriesTestCases, client, row + 1, 1)
        if row_value == "107":
            sheetsUtils.writeData(Locators.userStoriesTestCases, client, row + 1, 2, TestResults)
            written = True

    if written == False:
        new_row = ["107", TestResults, "", "", ""]
        sheetsUtils.appendData(Locators.userStoriesTestCases, client, new_row)


if __name__ == '__main_':
    unittest.main()
