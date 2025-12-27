import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



class LoginPage():
    login_emailid = By.ID,"input-email"
    login_password = By.ID,"input-password"
    login_button = By.XPATH,"//input[@value='Login']"
    edit_accountlink = By.XPATH,"//a[contains(text(),'Edit your account information')]"

    def __init__(self,driver):
        self.driver = driver

    def click_loginemail(self):
        self.driver.find_element(*self.login_emailid).send_keys("d55@yopmail.com")

    def click_loginpassword(self):
        self.driver.find_element(*self.login_password).send_keys("Test1234@")

    def click_loginbutton(self):
        self.driver.find_element(*self.login_button).click()

    def show_loginmessage(self):
        return (self.driver.find_element(*self.edit_accountlink)).text