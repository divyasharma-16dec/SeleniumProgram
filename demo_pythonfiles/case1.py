'''Test Case
-----------
1) Open Web Browser(Chrome/firefox/Edge).
2) Open URL  https://opensource-demo.orangehrmlive.com/
3) Enter username  (Admin).
4) Enter password  (admin123).
5) Click on Login.
6) Capture title of the home page.(Actual title)
7) Verify title of the page: OrangeHRM    (Expected)
8) close browser'''


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
#print the title
loginpage_title = driver.title
print("Title of login page is", loginpage_title)

driver.implicitly_wait(10)

#locators
username = driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
password = driver.find_element(By.XPATH,"//input[@name='password' and @placeholder='Password']").send_keys("admin123")
submit_login = driver.find_element(By.XPATH,"//button[@type='submit']").click()
#alert window
try:
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()
except:
    print("No alert window")

try:
    driver.find_element(By.LINK_TEXT,"Dashboard")
    print("Login successfully done!")
except:
    print("Login is not done.")

driver.close()