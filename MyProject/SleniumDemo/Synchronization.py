import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("Ber")
time.sleep(3)
result = driver.find_elements_by_xpath("//div[@class='products']/div")
count = result.__len__()
print(count)
assert count == 3
btns = driver.find_elements_by_xpath("//div[@class='product-action']/button")
prd_names = []
for btn in btns:
    prd_names.append(btn.find_element_by_xpath("parent::div/parent::div/h4").text)
    btn.click()
print("vegatbles list ", prd_names)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
prd_orderlist = driver.find_elements_by_css_selector("p[class=product-name]")
result_list = []
for prd in prd_orderlist:
    result_list.append(prd.text)
print("result list", result_list)
assert prd_names == result_list
amount = driver.find_element_by_css_selector(".discountAmt")
originalamout = amount.text
print(originalamout)
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
time.sleep(1)

driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
discamount = amount.text
print(discamount)
assert float(originalamout) > float(discamount)
msg = driver.find_element_by_css_selector(".promoInfo").text
print(msg)
allamount = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0.0
for amount in allamount:
    temp = amount.text
    sum = sum + float(temp)

print("product sum amount is ", sum)
totalamout = driver.find_element_by_css_selector(".totAmt").text
print("total amount"+totalamout)
assert sum == float(totalamout)

driver.close()
