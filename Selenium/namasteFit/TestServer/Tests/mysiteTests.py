# from namasteFit.TestServer.Pages.mysitePage import MySitePage
# from ..Pages.mysitePage import MySitePage
import time
import unittest
import HTMLTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from namasteFit.TestServer.Pages.mysitePage import MySitePage
from namasteFit.TestServer.Pages.loginPage import LoginPage
from namasteFit.TestServer.Pages.landingPage import LandingPage
from selenium import webdriver


class MySiteTests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        cls.driver.get("http://app.raawmove.com/mysite")
        cls.driver.maximize_window()
        return cls.driver

    def test_01_valid_login(self):
        driver = self.driver

        namaste_username = "nelly@namaste.fit"
        namaste_password = "qwertyui"

        loginpage = LoginPage(driver)
        loginpage.enterEmail(namaste_username)
        loginpage.enterPassword(namaste_password)
        loginpage.clickLogin()

    def test_02_click_mysite(self):
        driver = self.driver
        landingpage = LandingPage(driver)
        landingpage.clickMysite()

    def test_03_valid_instagram(self):
        driver = self.driver
        mysitepage = MySitePage(driver)
        mysitepage.inputInstagram("http://www.instagram.com/namaste_sample")
        mysitepage.clickPublishPage()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main_':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner('/Applications/MAMP/htdocs/AutomationTesting/Selenium/namasteFit/TestServer/Reports'))
