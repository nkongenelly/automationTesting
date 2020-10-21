import sys
import os
from selenium import webdriver
from namasteFit.TestServer.Locators.locators import Locators
from namasteFit.CommonFiles.blazeArgs import BlazeArgs
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
        self.options = webdriver.ChromeOptions()
        self.options.add_extension(extension=Locators.chrome_extension)
        # self.options.add_argument(['--disable-web-security', '--user-data-dir' + Locators.chrome_user_self.options, '--allow-running-insecure-content'])
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-save-passsword-bubble")
        self.options.add_argument('--user-data-dir' + Locators.chrome_user_profile)
        self.options.add_argument('--disable-web-security')
        self.options.add_argument('disable-infobars')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_experimental_option("useAutomationExtension", False)
        # self.options .setExperimentalOption("excludeSwitches", Collections.singletonList("enable-automatiion"))
        desired = DesiredCapabilities.CHROME

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }

        self.options.add_experimental_option('prefs', prefs)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # self.driver = webdriver.Chrome(options=self.options, executable_path=Locators.chrome_driver)

        # self.driver.get(Locators.testServer)
        # self.driver.maximize_window()


        ### BlazeGrid capabilites
        desired_capabilities = {
            'browserName': 'chrome',
            'blazemeter.sessionTimeout': '240',
        }

        blazegrid_url = 'https://{}:{}@{}/api/v4/grid/wd/hub'.format(self.API_KEY, self.API_SECRET, self.base)
        self.driver = webdriver.Remote(command_executor=blazegrid_url, desired_capabilities=desired_capabilities, options=self.options)

        blazeArgs = BlazeArgs()
        blazeArgs.blazemeterArgsStart(self.driver, "'namaste.fit connect with google test on Chrome'",
                                      "Accessing " + Locators.testServer)
        try:
            self.driver.get(Locators.testServer)
            blazeArgs.addArgs('passed', '')
        except AssertionError as exc:
            blazeArgs.addArgs('failed', '')
        except BaseException as exc:
            blazeArgs.addArgs('broken', '')
        blazeArgs.blazemeterArgsStop()

        return self.driver



    def firefoxTests(self):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--user-data-dir' + Locators.firefox_user_profile)
        self.options.set_preference("network.proxy.type", 1)
        self.options.set_preference("dom.webdriver.enabled", False)
        self.options.set_preference('useAutomationExtension', False)
        ### BlazeGrid capabilites
        desired_capabilities = {
            'browserName': 'firefox',
        'blazemeter.sessionTimeout':'240'}

        blazegrid_url = 'https://{}:{}@{}/api/v4/grid/wd/hub'.format(self.API_KEY, self.API_SECRET, self.base)
        self.driver = webdriver.Remote(command_executor=blazegrid_url, desired_capabilities=desired_capabilities, options=self.options)

        blazeArgs = BlazeArgs()
        blazeArgs.blazemeterArgsStart(self.driver, "'namaste.fit connect with google test on Firefox'",
                                      "Accessing " + Locators.testServer)
        try:
            self.driver.get(Locators.testServer)
            blazeArgs.addArgs('passed', '')
        except AssertionError as exc:
            blazeArgs.addArgs('failed', '')
        except BaseException as exc:
            blazeArgs.addArgs('broken', '')
        blazeArgs.blazemeterArgsStop()

        return self.driver

