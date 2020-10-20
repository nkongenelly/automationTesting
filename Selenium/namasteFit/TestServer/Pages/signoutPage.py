import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from ..Locators.locators import Locators

class SignoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.signout_button = Locators.signout_button_xpath


    def clicksSignout(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.signout_button_xpath)))
        # time.sleep(2)
        self.driver.find_element_by_xpath(self.signout_button_xpath).click()