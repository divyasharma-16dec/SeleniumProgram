from selenium import webdriver
from selenium.common import NoSuchElementException #safely handle missing elements
from selenium.webdriver.common.by import By  #By used to define locators
from utilities.RandomString import RandomData
from utilities.RandomString import fakedata

class TddRegisterPage():
    first_name = By.ID,"input-firstname"
    last_name = By.ID,"input-lastname"
    email_id = By.ID,"input-email"
    telephone_field = By.ID,"input-telephone"
    password_field = By.ID,"input-password"
    confirm_password = By.ID, "input-confirm"
    newsletter_field = By.XPATH,"//input[@name='newsletter' and @value=0]"
    privacy_policy = By.XPATH,"//input[@name='agree']"
    register_subimitbutton = By.XPATH,"//input[@type='submit']"
    validate_message = By.XPATH,"//h1[contains(text(),'Your Account Has Been Created!')]"
    warning_msg = By.XPATH, "//div[contains(@class,'alert-danger')]"


    def __init__(self,driver):
        self.driver=driver

    def register_elements(self,fn,ln,email,telephone,pw,cpw):
        self.driver.find_element(*self.first_name).send_keys(fn)
        self.driver.find_element(*self.last_name).send_keys(ln)
        self.driver.find_element(*self.email_id).send_keys(email)
        self.driver.find_element(*self.telephone_field).send_keys(telephone)
        self.driver.find_element(*self.password_field).send_keys(pw)
        self.driver.find_element(*self.confirm_password).send_keys(cpw)
        self.driver.find_element(*self.newsletter_field).click()
        self.driver.find_element(*self.privacy_policy).click()
        self.driver.find_element(*self.register_subimitbutton).click()




    def enter_firstname(self):
        self.driver.find_element(*self.first_name).send_keys(fakedata.randomFirstName())

    def enter_lastname(self):
        self.driver.find_element(*self.last_name).send_keys(fakedata.randomLastName())

    def enter_emailid(self):
        self.driver.find_element(*self.email_id).send_keys(fakedata.randomEmailId())

    def enter_telephone(self):
        self.driver.find_element(*self.telephone_field).send_keys(fakedata.randomtelephone())

    def enter_password(self):
        self.driver.find_element(*self.password_field).send_keys("Test1234@")

    def enter_confirmpassword(self):
        self.driver.find_element(*self.confirm_password).send_keys("Test1234@")

    def select_newsletters(self):
        self.driver.find_element(*self.newsletter_field).click()

    def click_privacypolicy(self):
        self.driver.find_element(*self.privacy_policy).click()

    def click_registersubmit(self):
        self.driver.find_element(*self.register_subimitbutton).click()

    def getconfirmationmessage(self):
        try:
            return self.driver.find_element(*self.validate_message).is_displayed()
        except NoSuchElementException:
            return False

    def warning_message(self):
        try:
            return "Warning" in self.driver.find_element(*self.warning_msg).text
        except NoSuchElementException:
            return False

