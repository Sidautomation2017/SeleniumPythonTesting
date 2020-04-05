import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ConfirmationPage import ConfirmationPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestPurchase(BaseClass):
    def test_purchase(self):
        log = self.getLogger(__name__)
        log.info("Test is started")
        hompage = HomePage(self.driver)
        checkoutpage = hompage.shopClick()
        log.info("User is navigated to production selction screen")
        checkoutpage.selectProduct()
        log.info("User has selcted production and navigated to checkout screen")
        confirmpage = ConfirmationPage(self.driver)
        confirmpage.purchaseItem()
        log.info("product is purchased successfully")