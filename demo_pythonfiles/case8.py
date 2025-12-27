
'''
import time

d1 = '26/01/1991'
d2 = '16/12/1992'

dep_date = time.strptime(d1, "%d/%m/%Y")
return_date = time.strptime(d2, "%d/%m/%Y")

print(return_date>dep_date)  # returns true/false '''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
date = driver.find_element(By.ID,"datepicker")
date.send_keys("05/30/2022")

month = 12
date = 16
year = 1992

date1 = driver.find_element(By.ID,"datepicker")
date1.click()


