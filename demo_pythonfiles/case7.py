from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
print(driver.title)

driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("test")
driver.switch_to.default_content()

