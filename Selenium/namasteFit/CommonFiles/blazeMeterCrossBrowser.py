import sys
import os
from selenium import webdriver
from namasteFit.TestServer.Locators.locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from namasteFit.TestServer.Locators.credentials import Credentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))


# from ..Locators.locators import Locators


class BlazeMeterCrossBrowserSignin():
    def __init__(self):
        self.API_KEY = Credentials.blazemeter_id
        self.API_SECRET = Credentials.blazemeter_secret
        self.base = 'a.blazemeter.com'

    def ChromeTests(self):
        ### BlazeGrid capabilites
        desired_capabilities = {
            'browserName': 'chrome'}

        blazegrid_url = 'https://{}:{}@{}/api/v4/grid/wd/hub'.format(self.API_KEY, self.API_SECRET, self.base)
        self.driver = webdriver.Remote(command_executor=blazegrid_url, desired_capabilities=desired_capabilities)
        return self.driver

    def firefoxTests(self):
        ### BlazeGrid capabilites
        desired_capabilities = {
            'browserName': 'firefox'}

        blazegrid_url = 'https://{}:{}@{}/api/v4/grid/wd/hub'.format(self.API_KEY, self.API_SECRET, self.base)
        self.driver = webdriver.Remote(command_executor=blazegrid_url, desired_capabilities=desired_capabilities)
        return self.driver

    def EdgeTests(self):
        ### BlazeGrid capabilites
        desired_capabilities = {
            'browserName': 'edge'}

        blazegrid_url = 'https://{}:{}@{}/api/v4/grid/wd/hub'.format(self.API_KEY, self.API_SECRET, self.base)
        self.driver = webdriver.Remote(command_executor=blazegrid_url, desired_capabilities=desired_capabilities)
        return self.driver
