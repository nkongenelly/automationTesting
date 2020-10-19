import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from ..Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_field = Locators.google_email_field_id
        self.email_field_next = Locators.google_emailnext_button_xpath
        self.pass_field = Locators.google_password_field_xpath
        self.pass_field_next = Locators.google_password_field_xpath


    def enterEmail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.email_field)))
        # time.sleep(2)
        self.driver.find_element_by_id(self.email_field).clear()
        emailField = self.driver.find_element_by_id(self.email_field)
        self.slow_typing(emailField, email)
        # self.driver.find_element_by_id(self.email_field).send_keys(email)

    def enterEmailNext(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.email_field_next)))
        self.driver.find_element_by_xpath(self.email_field_next).click()

    def enterPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.pass_field)))
        self.driver.find_element_by_id(self.pass_field).clear()
        passwordField = self.driver.find_element_by_id(self.pass_field)
        self.slow_typing(passwordField, password)
        # self.driver.find_element_by_id(self.pass_field).send_keys(password)

    def enterPasswordNext(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.pass_field_next)))
        self.driver.find_element_by_xpath(self.pass_field_next).click()

    def slow_typing(self, element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.01)



