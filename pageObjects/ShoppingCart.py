import pytest
from selenium import webdriver

import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(self.driver, 10)

        qty_element = wait.until(
            EC.element_to_be_clickable(self.update_qty)
        )

        qty_element.clear()
        qty_element.send_keys(qty)

        update_btn = wait.until(
            EC.element_to_be_clickable(self.update_btn)
        )
        update_btn.click()

    def quantity_successmessage(self):
        try:
            return self.driver.find_element(*self.qtyupdate_successmsg).is_displayed()
        except NoSuchElementException:
            return None

    def remove_product(self):
        self.driver.find_element(*self.delete_qty).click()
