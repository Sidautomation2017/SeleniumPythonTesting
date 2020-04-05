# JS Dom can access any element on webpage like selenium
from selenium import webdriver

path = "C:\\Users\\Sidheshwar.Tondare\\PycharmProjects\\MyProject\\BrowserDrivers\\ChromeDriver.exe"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Hello")
print(driver.title)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

btn=driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", btn)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

