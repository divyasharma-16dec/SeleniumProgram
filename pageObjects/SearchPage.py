import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchPage:
    #locators

    search_field = By.NAME,"search"
    search_button = By.XPATH,"//button[@class='btn btn-default btn-lg']"
    product_link = By.LINK_TEXT,"iMac"
    add_cart = By.ID,"button-cart"
    success_message = By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    cart_icon = By.XPATH,"//span[contains(text(),'Shopping Cart')]"
    shoppingcart_message = By.XPATH,"//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver

    def click_searchfield(self):
        self.driver.find_element(*self.search_field).clear()
        self.driver.find_element(*self.search_field).send_keys("mac")

    def click_searchbutton(self):
        self.driver.find_element(*self.search_button).click()

    def select_product(self):
        self.driver.find_element(*self.product_link).click()

    def addproduct_cart(self):
        self.driver.find_element(*self.add_cart).click()

    def get_successmessage(self):
        return  self.driver.find_element(*self.success_message).text

    def click_shoppingcart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_messageofshoppingcart(self):
        return self.driver.find_element(*self.shoppingcart_message).text


