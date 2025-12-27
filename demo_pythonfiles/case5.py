import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
multi_checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(multi_checkbox))
'''
#approatch 1 -- multi select
for checkboxes in multi_checkbox:
    checkboxes.click()

try:
    if checkboxes.is_enabled():
        print("All checkboxes are selected")
except:
    print("Checkboxes are not selected.")'''

'''
#approatch 2 -- firts three selction

for a in range(len(multi_checkbox)):
    if a<=2:
        multi_checkbox[a].click() '''

#approatch 3: specific selection

for check in multi_checkbox:
    weekname = check.get_attribute('id')
    if weekname == 'sunday' or weekname== 'tuesday':
        check.click()
        print("selcted day is", weekname)
    else:
        print("No days available")