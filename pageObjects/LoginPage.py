import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By



class LoginPage():
    login_emailid = By.ID,"input-email"
    login_password = By.ID,"input-password"
    login_button = By.XPATH,"//input[@value='Login']"
    edit_accountlink = By.XPATH,"//a[contains(text(),'Edit your account information')]"
    header_account  = By.XPATH,"//h2[text()='My Account']"
    header_accountlogout = By.XPATH,"//h1[text()='Account Logout']"
    warning_validtaion = By.XPATH,"//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver

    def click_loginemail(self,email):
        self.driver.find_element(*self.login_emailid).clear()
        self.driver.find_element(*self.login_emailid).send_keys(email)

    def click_loginpassword(self,password):
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(password)

    def click_normalloginemail(self):
        self.driver.find_element(*self.login_emailid).clear()
        self.driver.find_element(*self.login_emailid).send_keys("d55@yopmail.com")

    def click_normalloginpassword(self):
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys("Test1234@@")

    def login_elements(self,email,password):
        self.driver.find_element(*self.login_emailid).clear()
        self.driver.find_element(*self.login_emailid).send_keys(email)
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def click_loginbutton(self):
        self.driver.find_element(*self.login_button).click()



    def show_loginmessage(self):
        try:
            return "Edit your account information" in self.driver.find_element(*self.edit_accountlink).text
        except:
            return None


    def final_message(self):
        #return (self.driver.find_element(*self.header_account)).text
        try:
            return self.driver.find_element(*self.header_account).text
        except NoSuchElementException:
            return None

    def invalid_message(self):
        try:
            return self.driver.find_element(*self.warning_validtaion).text
        except NoSuchElementException:
            return None

    def logout_message(self):
        try:
            return self.driver.find_element(*self.header_accountlogout).text
        except NoSuchElementException:
            return None