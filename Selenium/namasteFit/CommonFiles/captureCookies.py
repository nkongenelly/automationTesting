import pickle
import selenium.webdriver
from namasteFit.TestServer.Locators.locators import Locators


class CaptureCookies():
    def __init__(self, driver):
        self.driver = driver

    def capture(self, driverName):
        # a = {driverName: self.driver.get_cookies()}
        # self.driver.get("http://www.google.com")
        # pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))
        # print(self.driver.get_cookies())

    def useCookies(self):
        # self.driver.get("http://www.google.com")
        self.driver.get(Locators.testServer)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            print("cookies")
            print(cookie)
            print(self.driver)
            print(cookies)
            self.driver.add_cookie(cookie)

        return self.driver
