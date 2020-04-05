from selenium import webdriver
from selenium.webdriver.support.select import Select

#path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
#driver = webdriver.Chrome(executable_path=path)
path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=path)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.current_url)
pageTitle = driver.title
print(pageTitle)
element = driver.find_element_by_name("name")
element.send_keys("Sidheshwar")
driver.find_element_by_name("email").send_keys("abc@gmail.com")
driver.find_element_by_css_selector("#exampleCheck1").click()
drop = driver.find_element_by_css_selector("select[id='exampleFormControlSelect1']")
select = Select(drop)
select.select_by_visible_text("Female")
status = driver.find_elements_by_xpath("//input[@name='inlineRadioOptions']")
print(status.__sizeof__())
for n in status:
    n.click()
driver.find_element_by_css_selector("input[type='submit']").click()
msg = driver.find_element_by_class_name("alert-success").text
print(msg)
assert "success" in msg
driver.close()
