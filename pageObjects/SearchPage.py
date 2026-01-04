import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException


class SearchPage:
    #locators

    search_field = By.NAME,"search"
    search_button = By.XPATH,"//button[@class='btn btn-default btn-lg']"
    list_button = By.ID,"list-view"
    invalidprodct_text =  By.XPATH,"//p[text() = 'There is no product that matches the search criteria.']"
    product_link = By.LINK_TEXT,"iMac"
    product_title= By.XPATH,"//div[@class='product-thumb']//h4/a"
    add_cart = By.ID,"button-cart"
    success_message = By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    cart_icon = By.XPATH,"//span[contains(text(),'Shopping Cart')]"
    shoppingcart_message = By.XPATH,"//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver

    def click_searchfield(self,keyword):
        self.driver.find_element(*self.search_field).clear()
        self.driver.find_element(*self.search_field).send_keys(keyword)

    def click_searchbutton(self):
        self.driver.find_element(*self.search_button).click()

    def show_listbutton(self):
        try:
            return self.driver.find_element(*self.list_button).is_displayed()
        except NoSuchElementException:
            return False

    def show_noproductmessage(self):
        try:
            return "no product" in self.driver.find_element(*self.invalidprodct_text).text
        except NoSuchElementException:
            return False

    def show_producttitle(self):
        try:
            elements = self.driver.find_elements(*self.product_title)
            return [ele.text for ele in elements]
        except NoSuchElementException:
            return []


    def select_product(self):
        self.driver.find_element(*self.product_link).click()

    def addproduct_cart(self):
        self.driver.find_element(*self.add_cart).click()

    def get_successmessage(self):
        try:
            return  self.driver.find_element(*self.success_message).text
        except:
            return None

    def click_shoppingcart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_messageofshoppingcart(self):
        try:
            return self.driver.find_element(*self.shoppingcart_message).text
        except:
            return None

