from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/login")

page_title = driver.title
print("Title is ", page_title)

email = driver.find_element(By.ID,"Email")
email.clear()
email.send_keys("admin@yourstore.com")

#get attribute or inner text

print("Email's text is", email.text)
print("Attribute is", email.get_attribute('value'))