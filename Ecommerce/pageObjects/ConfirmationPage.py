import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ConfirmationPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    location_select = (By.LINK_TEXT, "India")
    checkbox = (By.ID, "checkbox2")
    purchase_btn = (By.CSS_SELECTOR, "[class='btn btn-success btn-lg']")
    msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def purchaseItem(self):
        self.driver.find_element(*ConfirmationPage.location).send_keys("ind")
        self.waitForLinkPresent("India")
        location1 = self.driver.find_element(*ConfirmationPage.location_select)
        location1.click()
        time.sleep(2)
        checkbox1 = self.driver.find_element(*ConfirmationPage.checkbox)
        self.driver.execute_script("arguments[0].click();", checkbox1)
        self.driver.find_element(*ConfirmationPage.purchase_btn).click()
        message = self.driver.find_element(*ConfirmationPage.msg).text
        self.driver.get_screenshot_as_file("screen.png")
        print(message)
