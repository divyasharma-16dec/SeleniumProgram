import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

print(driver.current_url)
print(driver.title)

wait = WebDriverWait(driver,30)
wait1 = wait.until(EC.presence_of_element_located((By.ID, 'country')))

drpcountry=Select(driver.find_element(By.ID,'country'))
time.sleep(5)
drpcountry.select_by_visible_text("Japan")

length = drpcountry.options
print(len(length))
