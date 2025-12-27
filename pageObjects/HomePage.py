from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():
    my_accountlink = By.XPATH,"//a[@title='My Account']"
    register_link = By.LINK_TEXT,"Register"
    login_link = By.LINK_TEXT,"Login"
    logout_link = By.LINK_TEXT,"Logout"

    def __init__(self,driver):  #self = current object of Class
        self.driver = driver

    def click_accountlink(self):
        self.driver.find_element(*self.my_accountlink).click()

    def click_registerlink(self):
        self.driver.find_element(*self.register_link).click()

    def click_loginlink(self):
        self.driver.find_element(*self.login_link).click()

    def click_logoutlink(self):
        self.driver.find_element(*self.logout_link).click()

