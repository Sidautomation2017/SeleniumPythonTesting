from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    shop_item = (By.XPATH, "//div[@class='card h-100']")
    btn_add = (By.CSS_SELECTOR, "[class='nav-link btn btn-primary']")
    btn_checkout = (By.CSS_SELECTOR, "[class='btn btn-success']")

    def selectProduct(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        productslist = self.driver.find_elements(*CheckOutPage.shop_item)
        for product in productslist:
            name = product.find_element_by_xpath("div/h4").text
            print("product name" + name)
        if name == "Blackberry":
            product.find_element_by_xpath("div/button").click()
        self.driver.find_element(*CheckOutPage.btn_add).click()
        self.driver.find_element(*CheckOutPage.btn_checkout).click()
