import time

from selenium import webdriver

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("DEL")
time.sleep(2)
result = driver.find_elements_by_css_selector("p[class$='blackText']")
print(result.__len__())
for n in result:
    print(n.text)
    if n.text == "Dimapur, India":
        n.click()
        break

print("I am outside loop")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check_boxes = driver.find_elements_by_css_selector("input[type='checkbox']")
for checkbox in check_boxes:
    checkbox.click()
    assert checkbox.is_selected()
rediobtns = driver.find_elements_by_css_selector("input[type='radio']")
for rediobtn in rediobtns:
    rediobtn.click()

driver.find_element_by_name("enter-name").send_keys("Sidhesh")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element_by_id("confirmbtn").click()
alert1=driver.switch_to.alert
print(alert1.text)
alert1.dismiss()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

driver.close()