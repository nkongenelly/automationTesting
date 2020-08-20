import time
import unittest
# import HTMLTestRunner
import sys
import os
import time
import namasteFit.CommonFiles.excelUtils as XUtils

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from namasteFit.TestServer.Pages.loginPage import LoginPage
from namasteFit.TestServer.Pages.landingPage import LandingPage
from namasteFit.TestServer.Pages.mysitePage import MySitePage
from namasteFit.TestServer.Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
        login_button_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))

        email_field_element.clear()
        email_field_element.send_keys(namaste_username)

        pass_field_element.clear()
        pass_field_element.send_keys(namaste_password)

        login_button_element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, namaste_logo_xpath)))

    def test_page_refresh(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
        self.driver.refresh()
        url = self.driver.current_url
        time.sleep(3)
        self.assertEqual(url, self.driver.current_url, "The page should return to " + url)


if __name__ == '__main_':
    unittest.main()
