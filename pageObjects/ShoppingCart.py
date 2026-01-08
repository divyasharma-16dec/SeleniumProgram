import pytest
from selenium import webdriver

import os

from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
class ShoppingCart:

    cart_button = By.ID,'cart-total'
    view_cart = By.LINK_TEXT,'View Cart'
    checkout_btn = By.LINK_TEXT,'Checkout'
    product_name = By.XPATH,"//table[@class='table table-bordered']//td[2]/a"
    quantity_box= By.XPATH,"//input[contains(@name,'quantity')]"
    update_qty = By.XPATH,"//button[@type='submit']"
    delete_qty = By.XPATH,"//button[@class='btn btn-danger']"
    qtyupdate_successmsg= By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    outofstock_successmsg = By.XPATH,"//div[@class='alert alert-danger alert-dismissible']"
    emptycart_msg = By.XPATH,"//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.view_cart)).click()

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.product_name)
        ).text

    def update_quantity(self, qty):
        qty_input =  self.wait.until(EC.element_to_be_clickable(self.quantity_box))
        qty_input.clear()
        qty_input.send_keys(qty)
        return self.wait.until(EC.element_to_be_clickable(self.update_qty)).click()

    def message_addremove(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.qtyupdate_successmsg)
            ).text
        except TimeoutException:
            return None

    def remove_product(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_qty)).click()
