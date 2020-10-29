import sys
import os
import time
import timeit
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Selenium.namasteFit.TestServer.Locators.locators import Locators
from Selenium.namasteFit.CommonFiles.blazeArgs import BlazeArgs
from Selenium.namasteFit.CommonFiles.captureCookies import CaptureCookies

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
# from ..Locators.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_field = Locators.google_email_field_id
        self.email_field_next = Locators.google_emailnext_button_xpath
        self.pass_field = Locators.google_password_field_xpath
        self.pass_field_next = Locators.google_passwordnext_button_xpath


    def enterEmail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.email_field)))
        # time.sleep(2)
        self.driver.find_element_by_id(self.email_field).clear()
        emailField = self.driver.find_element_by_id(self.email_field)
        self.slow_typing(emailField, email)
        # self.driver.find_element_by_id(self.email_field).send_keys(email)

    def enterEmailNext(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field_next)))
        self.driver.find_element_by_xpath(self.email_field_next).click()

    def enterPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.pass_field)))
        self.driver.find_element_by_xpath(self.pass_field).clear()
        passwordField = self.driver.find_element_by_xpath(self.pass_field)
        self.slow_typing(passwordField, password)
        # self.driver.find_element_by_id(self.pass_field).send_keys(password)

    def enterPasswordNext(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.pass_field_next)))
        self.driver.find_element_by_xpath(self.pass_field_next).click()

    def slow_typing(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.01)

    def login(self, driverOption, driverName, email, password):
        self.driver = driverOption
        driver = self.driver
        print(driver)
        time.sleep(2)

        try:
            # Navigate to Login Page
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Locators.connect_with_google_xpath)))
            driver.find_element_by_xpath(Locators.connect_with_google_xpath).click()

            # Enter email and click next
            self.enterEmail(email)
            self.enterEmailNext()
            time.sleep(10)
            # start = timeit.timeit()
            # Enter password and click next
            self.enterPassword(password)
            self.enterPasswordNext()

            # end = timeit.timeit()

            time.sleep(10)
            # cookies = CaptureCookies(driver)
            # cookies.capture(driverName)
            # self.landingPage(end, start, driver)

            loginURL = driver.current_url
            print("Time taken to sign in is : ")
            # print(str(end - start))
            print("current URl = ")
            print(loginURL)
            # self.loginMessageResults(loginURL)
            result = ""
            # "Get cookies"
            cookies_list = driver.get_cookies()
            cookies_dict = {}
            for cookie in cookies_list:
                cookies_dict[cookie['name']] = cookie['value']
            print("COOKIES ARE: ")
            print(cookies_dict)
            return cookies_dict

            # blazeArgs = BlazeArgs()
            # result = blazeArgs.blazemeterArgsStart(driver, "'namaste.fit landing page'",
            #                               "landing message for this account is " + loginURL)
            #
            # message = driverName + "browser status message for this account is : " + result
            # return cookies_dict

        except Exception as e:
            result = "LOGIN FAILED"
            print('Login Failed')
            print(str(e))
            time.sleep(3)
            # driver.close()
            message = driverName + "browser status message for this account is : " + result

            return message

    def loginMessageResults(self, loginURL):
        a = Locators.testServer
        landingPages = my_dictionary()
        landingPages['pages'] = {1: "home", 2: "/home/get-started", 3: "/home/get-started"}
        landingPages['status'] = {1: "passed", 2: "failed", 3: "broken"}
        landingPages['messages'] = {"YOU HAVE NO ACCESS TO THE STUDIO PLATFORM", "PLEASE PUBLISH YOUR STUDIO FIRST",
                                    "WELCOME BACK TO YOUR STUDIO PLATFORM"}

        landingPages['testSuiteName'] = {1:"Test for non- registered emails", 2:"Test for first time users landing page",3:"Test for second time studio owners"}
        landingPages['testCaseName'] = {1:"Non-registered emails should not access the platform",2:"First time users should land on my studio page",3:"Second time user lands on get-started page"}

        count = 1
        blazeArgs = BlazeArgs()
        for landedPage in landingPages:

            blazeArgs.blazemeterArgsStart(self.driver, landingPages['testSuiteName'][count],
                                          landingPages['testCaseName'][count] + loginURL)
            try:
                if loginURL == landingPages['pages'][count]:
                    result = landingPages['messages'][count]
                    print(result)
                    blazeArgs.addArgs(landingPages['status'][1], result)
            except AssertionError as exc:
                blazeArgs.addArgs(landingPages['status'][2], '')
            except BaseException as exc:
                blazeArgs.addArgs(landingPages['status'][3], '')
            blazeArgs.blazemeterArgsStop()


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value

