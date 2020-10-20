import sys
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from namasteFit.TestServer.Locators.locators import Locators
from namasteFit.TestServer.Locators.accounts import Accounts
from namasteFit.TestServer.Pages.signoutPage import SignoutPage
# from .test_google import Google

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

# Site customize
class Signout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = Locators.chrome_driver)
        # self.driver.get(Locators.testServer + 'home/get-started')
        # self.driver.maximize_window()
        return self.driver


    def test_login(self):
        driver = self.driver
        time.sleep(2)
        # googleSignin = Google()
        print("Sign in results is = ")
        # print(googleSignin)

