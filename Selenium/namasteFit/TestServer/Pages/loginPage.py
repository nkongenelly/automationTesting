import sys
import os
import time
import timeit
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from namasteFit.TestServer.Locators.locators import Locators

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
            time.sleep(3)
            start = timeit.timeit()
            # Enter password and click next
            self.enterPassword(password)
            self.enterPasswordNext()

            end = timeit.timeit()

            time.sleep(5)
            # self.landingPage(end, start, driver)

            loginURL = driver.current_url
            print("Time taken to sign in is : ")
            print(end - start)
            print("current URl = ")
            print(loginURL)

            if loginURL == Locators.testServer:
                result = "YOU HAVE NO ACCESS TO THE STUDIO PLATFORM"
                print(result)

            elif loginURL == Locators.testServer + "/home/studio":
                result = "PLEASE PUBLISH YOUR STUDIO FIRST"
                print(result)

            elif loginURL == Locators.testServer + "/home/get-started":
                result = "WELCOME BACK TO YOUR STUDIO PLATFORM"
                print(result)

            # driver.close()
            # time.sleep(5)
            message = driverName + "browser status message for this account is : " + result + "\n And login in time is :" + end -start + " seconds"
            return message

        except Exception as e:
            result = "LOGIN FAILED"
            print('Login Failed')
            print(str(e))
            time.sleep(3)
            # driver.close()
            message = driverName + "browser status message for this account is : " + result + " \n And login in time is :" + str(end - start) + " seconds"

            return message



