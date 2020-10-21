# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Record102120100729Am(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://Python38//chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_record102120100729_am(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1357,647 | ]]
        driver.get("http://app.namastefit.one/")
        # Label: Sign in with google
        driver.find_element_by_css_selector("a.MuiButtonBase-root.MuiButton-root.MuiButton-text.jss246").click()
        driver.get(
            "https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=select_account&response_type=code&redirect_uri=http%3A%2F%2Fapp.namastefit.one%2Fauth%2Fgoogle%2Fcallback&scope=profile%20email&client_id=736316595070-ln9rp9l4lrnobesa9imb53uvmd5mepds.apps.googleusercontent.com")
        driver.find_element_by_xpath("(//div[@id='profileIdentifier'])[3]").click()
        driver.get("http://app.namastefit.one/")
        # ERROR: Caught exception [ERROR: Unsupported command [openWindow | https://www.google.com/search?sxsrf=ALeKk03wNg8fAzn8O9lUAK_w2LRI9yzqZw%3A1603250365902&ei=vaiPX-PFNpCv9QP7r5GYDA&q=blazemeter+mobile+browser+python+selenium+code&oq=blazemeter+mobile+browser+python+selenium+code&gs_lcp=CgZwc3ktYWIQAzIHCCEQChCgAToECCMQJzoKCAAQsQMQyQMQCjoECAAQCjoLCAAQsQMQyQMQkQI6BQgAEJECOgIIADoICAAQyQMQkQI6BQgAEMkDOgcIABAUEIcCOgYIABAWEB46BQghEKABOggIIRAWEB0QHjoECCEQFVDzwAFYvKUCYICnAmgCcAB4AIAB4wKIAeRCkgEJMC4yOC4xNC4xmAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwijmK6E3cTsAhWQV30KHftXBMMQ4dUDCA0&uact=5 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
        # Label: Add Studio
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/nav/div[2]/div/div/div/ul/div/a[2]/div[2]/span").click()
        driver.find_element_by_id("domain").click()
        driver.find_element_by_id("domain").clear()
        driver.find_element_by_id("domain").send_keys("nellyyoga")
        driver.find_element_by_id("name").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("Nelly")
        driver.find_element_by_id("domain").clear()
        driver.find_element_by_id("domain").send_keys("Nelly")
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys("Rajkot")
        driver.find_element_by_id("state").clear()
        driver.find_element_by_id("state").send_keys("Gujarat")
        driver.find_element_by_id("country").clear()
        driver.find_element_by_id("country").send_keys("India")
        driver.find_element_by_id("about").click()
        driver.find_element_by_id("about").clear()
        driver.find_element_by_id("about").send_keys("Nelly")
        driver.find_element_by_id("domain").click()
        driver.find_element_by_id("domain").clear()
        driver.find_element_by_id("domain").send_keys("nellyyoga")
        driver.find_element_by_id("about").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        # Label: Upload cover photo
        driver.find_element_by_css_selector(
            "button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.jss217.MuiButton-outlinedPrimary.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_xpath("(//img[@alt='Cover Image Tile'])[8]").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_css_selector(
            "button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.jss300.MuiButton-outlinedPrimary.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > label > span.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-colorPrimary > span.MuiIconButton-label").click()
        # Label: Upload profile image
        driver.find_element_by_id("profile-image-upload").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_css_selector(
            "span.MuiTypography-root.MuiListItemText-primary.MuiTypography-body1.MuiTypography-displayBlock").click()
        driver.find_element_by_css_selector(
            "h4.MuiTypography-root.MuiTypography-h4.MuiTypography-colorPrimary.MuiTypography-gutterBottom").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/nav/div[2]/div/div/div/ul/div/a[3]/div[2]/span").click()
        # Label: create event
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/nav/div[2]/div/div/div/ul/div/a[3]/div[2]/span").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_id("outlined-basic").click()
        driver.find_element_by_id("outlined-basic").clear()
        driver.find_element_by_id("outlined-basic").send_keys("Yoga 101")
        driver.find_element_by_id("outlined-multiline-static").click()
        driver.find_element_by_id("outlined-multiline-static").clear()
        driver.find_element_by_id("outlined-multiline-static").send_keys("Yoga 101")
        driver.find_element_by_name("confLink").click()
        driver.find_element_by_name("confLink").clear()
        driver.find_element_by_name("confLink").send_keys("https://zoom.us/")
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        # Label: Edit event
        driver.find_element_by_css_selector(
            "button.MuiButtonBase-root.MuiButton-root.MuiButton-outlined.MuiButton-outlinedPrimary.MuiButton-outlinedSizeLarge.MuiButton-sizeLarge.MuiButton-fullWidth > span.MuiButton-label").click()
        driver.find_element_by_name("freeEvent").click()
        driver.find_element_by_name("freeEvent").clear()
        driver.find_element_by_name("freeEvent").send_keys("false")
        driver.find_element_by_id("standard-adornment-amount").click()
        driver.find_element_by_id("standard-adornment-amount").clear()
        driver.find_element_by_id("standard-adornment-amount").send_keys("50")
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_name("freeEvent").click()
        driver.find_element_by_name("freeEvent").clear()
        driver.find_element_by_name("freeEvent").send_keys("true")
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_css_selector(
            "li.MuiButtonBase-root.MuiListItem-root.MuiMenuItem-root.MuiMenuItem-gutters.MuiListItem-gutters.MuiListItem-button").click()
        driver.find_element_by_css_selector(
            "div.MuiFormControl-root.MuiFormControl-fullWidth > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge > span.MuiButton-label").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/nav/div[2]/div/div/div/ul/div/a[5]/div[2]/span").click()
        driver.find_element_by_xpath(
            "//div[@id='root']/div/div[2]/nav/div[2]/div/div/div/ul/div/a[6]/div[2]/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
