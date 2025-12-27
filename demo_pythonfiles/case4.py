from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
'''
driver.get("https://demo.nopcommerce.com/")

links = driver.find_elements(By.XPATH,'//a')
print(len(links))

for link in links:
    print(link.text)
'''

