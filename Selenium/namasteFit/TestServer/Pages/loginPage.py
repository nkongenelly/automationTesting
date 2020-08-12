import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from ..Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_field = Locators.email_field_id
        self.pass_field = Locators.pass_field_id
        self.login_button = Locators.login_button_xpath

    def enterEmail(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.email_field)))
        self.driver.find_element_by_id(self.email_field).clear()
        self.driver.find_element_by_id(self.email_field).send_keys(email)

    def enterPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.pass_field)))
        self.driver.find_element_by_id(self.pass_field).clear()
        self.driver.find_element_by_id(self.pass_field).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.login_button)))
        self.driver.find_element_by_xpath(self.login_button).click()