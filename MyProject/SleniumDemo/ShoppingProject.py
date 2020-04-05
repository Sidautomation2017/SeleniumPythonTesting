import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    name = product.find_element_by_xpath("div/h4").text
    print("product name"+name)
    if name == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
time.sleep(2)
checkbox = driver.find_element_by_id("checkbox2")
driver.execute_script("arguments[0].click();", checkbox)
driver.find_element_by_css_selector("[class='btn btn-success btn-lg']").click()
msg = driver.find_element_by_css_selector("[class*='alert-success']").text
driver.get_screenshot_as_file("screen.png")
print(msg)
driver.close()
