import time

from selenium import webdriver

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
pwindow = driver.current_window_handle;
windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    print(driver.find_element_by_tag_name("h3").text)
    if window != pwindow:
        driver.close()

driver.switch_to.window(pwindow)
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("I am autoamtion frames")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)