import sys
import os
from selenium import webdriver
from namasteFit.TestServer.Locators.locators import Locators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))


# from ..Locators.locators import Locators


class CrossBrowserSignin():

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
        self.driver = webdriver.Chrome(options=self.options, executable_path=Locators.chrome_driver)

        self.driver.get(Locators.testServer)
        self.driver.maximize_window()

        # self.login(self.driver)

        return self.driver

    def firefoxTests(self):
        # self.driver = webdriver.Firefox(executable_path=Locators.firefox_driver)
        # # driver = webdriver.Firefox()
        # self.driver.get(Locators.testServer)
        # self.driver.maximize_window()
        # time.sleep(10)

        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--user-data-dir' + Locators.firefox_user_profile)
        # PROXY_HOST = "12.12.12.123"
        # PROXY_PORT = "1234"
        self.options.set_preference("network.proxy.type", 1)
        # self.options.set_preference("network.proxy.http", PROXY_HOST)
        # self.options.set_preference("network.proxy.http_port", int(PROXY_PORT))
        self.options.set_preference("dom.webdriver.enabled", False)
        self.options.set_preference('useAutomationExtension', False)
        # self.options.update_preference()
        # self.options.update_preferences()
        desired = DesiredCapabilities.FIREFOX

        # self.driver = webdriver.Firefox(firefox_profile=self.options, desired_capabilities=desired, executable_path=Locators.firefox_driver)
        self.driver = webdriver.Firefox(options=self.options, desired_capabilities=desired,
                                        executable_path=Locators.firefox_driver)
        # self.driver = webdriver.Firefox(options=self.options, executable_path=Locators.firefox_driver)

        self.driver.set_page_load_timeout(20)
        self.driver.get(Locators.testServer)
        while True:
            try:
                # self.driver.get(Locators.testServer)
                self.driver.maximize_window()
            except TimeoutException:
                print
                "Timeout, retrying..."
                continue
            else:
                break

        return self.driver
