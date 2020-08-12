# from ..Locators.locators import Locators
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from ..Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MySitePage:
    def __init__(self, driver):
        self.driver = driver
        self.instagram_textbox = Locators.instagram_textbox_id
        self.facebook_textbox = Locators.facebook_textbox_id
        self.youtube_textbox = Locators.youtube_textbox_id
        self.website_textbox = Locators.website_textbox_id
        self.publish_button = Locators.publish_button_xpath

    def inputInstagram(self, instagram):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.instagram_textbox)))
        self.driver.find_element_by_id(self.instagram_textbox).clear()
        self.driver.find_element_by_id(self.instagram_textbox).send_keys(instagram)

    def clickPublishPage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.publish_button)))
        self.driver.find_element_by_xpath(self.publish_button).click()
