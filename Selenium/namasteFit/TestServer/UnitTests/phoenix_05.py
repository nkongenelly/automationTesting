import time
import unittest
import traceback
import sys
import os
import time
# import namasteFit.CommonFiles.excelUtils as XUtils
# import gspread
# import namasteFit.CommonFiles.googleSheetsUtils as sheetsUtils
# from oauth2client.service_account import ServiceAccountCredentials
from namasteFit.TestServer.Pages.landingPage import LandingPage
from namasteFit.TestServer.UnitTests.test_valid_login import LoginTest
from namasteFit.TestServer.Pages.mysitePage import MySitePage
from namasteFit.TestServer.Locators.locators import Locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

TestResults = ""
drivers = []
user_story = "107"

# Site customize
class Phoenix_05(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", Locators.chrome_mobile_emulation)

        drivers.append({"webdriver": webdriver.Firefox, "executable_path": Locators.firefox_driver})
        drivers.append({"webdriver": webdriver.Chrome, "executable_path": Locators.chrome_driver})
        drivers.append({"webdriver": webdriver.ChromeOptions, "executable_path": Locators.chrome_driver, "chrome_options":chrome_options})
        drivers.append({"webdriver": webdriver.Edge, "executable_path": Locators.microsoft_edge_driver})


    def test_107(self):
        # for browser in drivers:
        for index, browser in enumerate(drivers):
            for driver in drivers:
                print(driver)
            if index == "2":
                print("index == " , index)
                self.driver = browser["webdriver"](executable_path=browser["executable_path"], chrome_option=browser["chrome_options"])

            self.driver = browser["webdriver"](executable_path=browser["executable_path"])
            # for
            self.driver.get(Locators.testServer + Locators.login_url)
            self.driver.maximize_window()
            driver = self.driver

            # chrome_options = Options()
            # chrome_options.add_argument(
            #     '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
            # driver = webdriver.Chrome(options=chrome_options)
            # driver.get('https://www.google.com')

            # Login email_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, email_field_id)))
            namaste_username = Locators.namaste_username
            namaste_password = Locators.namaste_password
            email_field_id = Locators.email_field_id
            pass_field_id = Locators.pass_field_id
            login_button_xpath = Locators.login_button_xpath
            namaste_logo_xpath = Locators.namaste_logo_xpath

            email_field_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, email_field_id)))
            pass_field_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, pass_field_id)))
            login_button_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, login_button_xpath)))

            email_field_element.clear()
            email_field_element.send_keys(namaste_username)

            pass_field_element.clear()
            pass_field_element.send_keys(namaste_password)

            login_button_element.click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, namaste_logo_xpath)))

            # def test_page_refresh(self):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
            # url_getstarted = driver.current_url
            # driver.refresh()

            # test PHOENIX -5
            time.sleep(5)
            get_started_text_xpath = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.get_started_text_xpath)))
            print("get_started_text_xpath = ", get_started_text_xpath)
            my_site_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.mysite_button_id)))
            print("my_site_id = ", my_site_id)
            my_events_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.my_events_button_id)))
            print("my_events_id = ", my_events_id)
            create_events_xpath = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.create_events_button_id)))
            print("create_events_xpath = ", create_events_xpath)
            members_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.members_button_id)))
            print("members_id = ", members_id)
            manage_payments_id = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.manage_payments_id)))
            print("manage_payments_id = ", manage_payments_id)

            if get_started_text_xpath != "null":
                element = driver.find_element_by_xpath(Locators.get_started_text_xpath)
                get_started_text_xpath.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.main_url);
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.customize_my_site_button_xpath)))
                element_find = driver.find_elements_by_xpath(Locators.customize_my_site_button_xpath)
                for value in element_find:
                    # print("get_started_text_xpath element.text", value.text)
                    # print("get_started_text_xpath element.text", element_find.text)
                    assert value.text == Locators.customize_my_site_button_text

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.setup_events_button_xpath)))
                element_find2 = driver.find_elements_by_xpath(Locators.setup_events_button_xpath)
                for value in element_find2:
                    assert value.text == Locators.setup_events_button_text

            if my_site_id != "null":
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, Locators.mysite_button_id)))
                # element = driver.find_element_by_id(Locators.mysite_button_id)
                element.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.mysites);
                element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.mysite_button_text_xpath)))
                assert element1.text == Locators.mysite_button_text

            if my_events_id != "null":
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, Locators.my_events_button_id)))
                # element = driver.find_element_by_id(Locators.my_events_button_id)
                element.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.myevents);
                element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.my_events_button_text_xpath)))
                assert element1.text == Locators.my_events_button_text

            if create_events_xpath != "null":
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, Locators.create_events_button_id)))
                # element = driver.find_element_by_id(Locators.create_events_button_id)
                element.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.createevents);
                element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.create_events_button_text_xpath)))
                assert element1.text == Locators.create_events_button_text

            if members_id != "null":
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, Locators.members_button_id)))
                # element = driver.find_element_by_id(Locators.members_button_id)
                element.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.members);
                element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.members_button_text_xpath)))
                assert element1.text == Locators.members_button_text

            if manage_payments_id != "null":
                wait = WebDriverWait(driver, 10)
                element = wait.until(EC.element_to_be_clickable((By.ID, Locators.manage_payments_id)))
                # element = driver.find_element_by_id(Locators.manage_payments_id)
                element.click()
                url_getstarted = driver.current_url
                self.assertEquals(url_getstarted, Locators.testServer + Locators.managePayments);
                element1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.manage_payments_text_xpath)))
                assert element1.text == Locators.manage_payments_text



    def tearDown(self) -> None:
        self.driver.close()
