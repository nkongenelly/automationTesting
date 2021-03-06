import time
import unittest
import HTMLTestRunner
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

class LoginUnitTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        cls.driver.get(Locators.testServer +"login")
        cls.driver.maximize_window()
        return  cls.driver

    def test_01_data_driven_login(self):
        driver = self.driver
        loginpage = LoginPage(driver)
        landingpage = LandingPage(driver)

        path = "/Users/nellynkonge/Documents/Documents – Nelly’s MacBook Pro/Nelly/QA/Data Driven Excels/loginDataTests.xlsx"
        rows = XUtils.getRowCount(path, 0)
        for r in range(2,rows + 1):
            namaste_username = XUtils.readData(path, 0, r, 1)
            namaste_password = XUtils.readData(path, 0, r, 2)
            print(namaste_username + "    ,   " + namaste_password)

            loginpage.enterEmail(namaste_username)
            time.sleep(2)
            loginpage.enterPassword(namaste_password)
            loginpage.clickLogin()
            print("isLogginSuccessful = " )
            print(landingpage.isLoginSuccessful())

            time.sleep(3)
            if landingpage.isLoginSuccessful():
                XUtils.writeData(path, 0, r, 5, "PASS")
                landingpage.signOut()
                print("Login Successful")
                time.sleep(1)

            elif not landingpage.isLoginSuccessful():
                XUtils.writeData(path, 0, r, 5, "FAIL")
                print("Login Failed")
                time.sleep(1)

        # time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main_':
    unittest.main()