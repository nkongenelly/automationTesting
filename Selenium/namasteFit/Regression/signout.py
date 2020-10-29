import sys
import os
import unittest
import time
from selenium import webdriver
from Selenium.namasteFit.TestServer.Locators.locators import Locators
from Selenium.namasteFit.CommonFiles.captureCookies import CaptureCookies

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

# Site customize
class Signout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = Locators.chrome_driver)

        cookies = CaptureCookies(self.driver)
        time.sleep(4)
        driverCookies = cookies.useCookies()
        time.sleep(5)
        self.driver.get(Locators.testServer + 'home/get-started')
        self.driver = driverCookies
        self.driver.maximize_window()
        print("DRIVER COOKIES = ")
        print(self.driver)
        # return driverCookies
        return self.driver


    def test_login(self):
        driver = self.driver
        time.sleep(2)
        # googleSignin = Google()
        print("Sign in results is = ")
        # print(googleSignin)

