import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from ..Locators.locators import Locators

class LandingPage():
    def __init__(self,driver):
        self.driver = driver
        self.mysite_button = Locators.mysite_button_id

    def clickMysite(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.mysite_button)))
        self.driver.find_element_by_id(self.mysite_button).click()