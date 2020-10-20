import getpass
import sys
import os
import timeit
import unittest
import time
from filecmp import cmp

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from ..TestServer.Locators.locators import Locators
# from ..TestServer.Pages.loginPage import LoginPage
from namasteFit.TestServer.Locators.locators import Locators
from namasteFit.CommonFiles.crossBrowserSignin import CrossBrowserSignin
from namasteFit.TestServer.Locators.accounts import Accounts
from namasteFit.TestServer.Pages.loginPage import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
# unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: cmp(y, x)

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

    # Main Function


# dict_obj = my_dictionary()

class Google(unittest.TestCase):
    def setUp(self):
        print('Enter the gmailid and password')
        # self.email, self.password = map(str, input().split())
        self.email = input("Enter email: ")
        self.password = input('Input password: ')
        # self.password = getpass.getpass('Input password: ')
        # self.ChromeTests()
        # self.firefoxTests()
        crossbrowser = CrossBrowserSignin()
        chrome_driver = crossbrowser.ChromeTests()
        chrome_mobile_driver = crossbrowser.ChromeMobileTests()
        firefox_driver = crossbrowser.firefoxTests()
        edge_driver = crossbrowser.EdgeTests()
        self.drivers = my_dictionary()
        self.drivers['chrome'] = chrome_driver
        self.drivers['chrome'] = chrome_mobile_driver
        self.drivers['firefox'] = firefox_driver
        self.drivers['edge'] = edge_driver

        print("ALL DRIVERS = ")
        for driver in self.drivers.values():
            print(driver)
        return self.drivers
        # drivers.append(firefox_driver)


    def test_login(self):
        for driverOptions in self.drivers.values():
            # time.sleep(10)
            print("again")
            print(driverOptions)
            self.driver = driverOptions
            driver = self.driver
            print(driver)
            time.sleep(2)
            # Define variables
            email = self.email
            password = self.password
            # print('Enter the gmailid and password')
            # email, password = map(str, input().split())

            # email = Accounts.email
            # password = Accounts.password

            try:
                # Navigate to Login Page
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, Locators.connect_with_google_xpath)))
                driver.find_element_by_xpath(Locators.connect_with_google_xpath).click()



                # Enter email and click next
                loginPage = LoginPage(driver)

                loginPage.enterEmail(email)
                loginPage.enterEmailNext()
                time.sleep(3)
                start = timeit.timeit()
                # Enter password and click next
                loginPage.enterPassword(password)
                loginPage.enterPasswordNext()

                end = timeit.timeit()

                time.sleep(10)
                # self.landingPage(end, start, driver)

                loginURL = driver.current_url
                print("Time taken to sign in is : ")
                print(end - start)
                print("current URl = ")
                print(loginURL)

                if loginURL == Locators.testServer:
                    print("YOU HAVE NO ACCESS TO THE STUDIO PLATFORM")

                elif loginURL == Locators.testServer + "/home/studio":
                    print("PLEASE PUBLISH YOUR STUDIO FIRST")

                # driver.close()
                time.sleep(5)
                # self.firefoxTests()

            except Exception as e:
                print('Login Failed')
                print(str(e))
                # logger.error('Failed to upload to ftp: ' + str(e))

                # driver.close()

    # def landingPage(self, end, start, driver):
    #     # driver = self.driver
    #     # get URl after successful login
    #     loginURL = driver.current_url
    #     print("Time taken to sign in is : ")
    #     print(end - start)
    #     print("current URl = ")
    #     print(loginURL)
    #
    #     if loginURL == Locators.testServer:
    #         print("YOU HAVE NO ACCESS TO THE STUDIO PLATFORM")
    #
    #     elif loginURL == Locators.testServer+"/home/studio":
    #         print("PLEASE PUBLISH YOUR STUDIO FIRST")
    #
    #     driver.close()
    #     time.sleep(5)
    #     self.firefoxTests()
    #
    #     # Assertain successful login logo exists
    #     # WebDriverWait(self.driver, 10).until(
    #     #     EC.presence_of_element_located((By.XPATH, Locators.successful_login_logo_xpath)))
    #     # namasteLogo = driver.find_elements(By.TAG_NAME, 'img')
    #     #
    #     # for image in namasteLogo:
    #     #     current_link = image.get_attribute("src")
    #     #     print("current_link")
    #     #     assert current_link == "/static/media/logo.e1ae6d8b.png"
    #     #     print(current_link)
    #     #     self.assertEqual("/static/media/logo.e1ae6d8b.png", current_link)




    # def tearDown(self) -> None:
    #     self.driver.close()

if __name__ == '__main_':
    unittest.main()