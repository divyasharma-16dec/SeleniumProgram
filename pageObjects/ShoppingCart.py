import pytest
from selenium import webdriver

import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ShoppingCart:

    cart_button = By.ID,'cart-total'
    view_cart = By.LINK_TEXT,'View Cart'
    checkout_btn = By.LINK_TEXT,'Checkout'
    product_name = By.XPATH,"//table[@class='table table-bordered']//td[2]/a"
    quantity_box= By.XPATH,"//input[contains(@name,'quantity')]"
    update_qty = By.XPATH,"//button[@class='btn btn-primary']"
    delete_qty = By.XPATH,"//button[@class='btn btn-danger']"
    qtyupdate_successmsg= By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    outofstock_successmsg = By.XPATH,"//div[@class='alert alert-danger alert-dismissible']"
    emptycart_msg = By.XPATH,"//p[contains(text(),'Your shopping cart is empty!')]"

    def __init__(self,driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()
        try:
            return self.driver.find_element(*self.view_cart).click()
        except NoSuchElementException:
            return None, self.driver.find_element(*self.emptycart_msg).text

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    def update_quantity(self, qty):
        box = self.driver.find_element(*self.quantity_box)
        box.clear()
        box.send_keys(qty)
        self.driver.find_element(*self.update_qty).click()

    def quantity_successmessage(self):
        try:
            return self.driver.find_element(*self.qtyupdate_successmsg).is_displayed()
        except NoSuchElementException:
            return False

    def remove_product(self):
        self.driver.find_element(*self.delete_qty).click()
