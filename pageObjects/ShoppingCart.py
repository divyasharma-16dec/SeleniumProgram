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
        self.wait = WebDriverWait(driver, 15)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.view_cart)).click()

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.product_name)
        ).text

    def update_quantity(self, qty):
        qty_input = self.wait.until(
            EC.visibility_of_element_located(self.quantity_box)
        )
        qty_input.clear()
        qty_input.send_keys(qty)

        self.wait.until(
            EC.element_to_be_clickable(self.update_qty)
        ).click()

    def quantity_successmessage(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.qtyupdate_successmsg)
            ).is_displayed()
        except:
            return False

    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.delete_qty)
        ).click()

        # IMPORTANT: wait for page refresh / DOM update
        self.wait.until(
            EC.staleness_of(
                self.driver.find_element(By.XPATH, "//table[contains(@class,'table-bordered')]")
            )
        )

    def is_cart_table_empty(self):
        rows = self.driver.find_elements(
            By.XPATH, "//table[contains(@class,'table-bordered')]//tbody/tr"
        )
        return len(rows) == 0
