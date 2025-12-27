from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10) #wait declaration

driver.maximize_window()
driver.get("https://www.google.com/")

search = driver.find_element(By.ID,"APjFqb")
search.send_keys("Latest MacBook")

google_search = driver.find_element(By.NAME,"btnK").click()