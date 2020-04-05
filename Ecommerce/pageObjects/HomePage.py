from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopClick(self):
        self.driver.find_element(*HomePage.shop).click()  # deserialize tuple you need to use
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage

    def form_Submission(self, name, email, gender):
        element = self.driver.find_element_by_name("name")
        element.send_keys(name)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_css_selector("#exampleCheck1").click()
        drop = self.driver.find_element_by_css_selector("select[id='exampleFormControlSelect1']")
        select = Select(drop)
        select.select_by_visible_text(gender)
        status = self.driver.find_elements_by_xpath("//input[@name='inlineRadioOptions']")
        print(status.__sizeof__())
        for n in status:
            n.click()
        self.driver.find_element_by_css_selector("input[type='submit']").click()
        msg = self.driver.find_element_by_class_name("alert-success").text
        print(msg)
        assert "success" in msg
        self.driver.refresh()

