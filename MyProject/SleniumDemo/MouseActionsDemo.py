
from selenium import webdriver
from selenium.webdriver import ActionChains

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get("https://chercher.tech/practice/popups")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("sub-menu")).perform()
action.move_to_element(driver.find_element_by_id("link1")).click().perform()
driver.back()
driver.get("https://chercher.tech/practice/popups")
action1 = ActionChains(driver)
action1.context_click(driver.find_element_by_id("double-click")).perform()
action1.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()




