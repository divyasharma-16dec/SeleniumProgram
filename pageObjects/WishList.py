import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class WishList:
    search_field = By.NAME,"search"
    serach_btn = By.XPATH,"//button[@class='btn btn-default btn-lg']"
    product_detail = By.XPATH,"//div[@class='image']//img[@title='iMac']"
    wishlist_btn = By.XPATH,"//div[@id='product-product']//div[@class='btn-group']//button[1]"
    wishlist_success = By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    wishlist_mainbtn = By.XPATH, "//a[@id='wishlist-total']"
    title_wishlist = By.XPATH, "//h2[normalize-space()='My Wish List']"
    cart_btn = By.XPATH,"//button[@class='btn btn-primary']//i[@class='fa fa-shopping-cart']"
    cartorremove_success= By.XPATH,"//div[@class='alert alert-success alert-dismissible']"
    delete_btn = By.XPATH,"//a[@class='btn btn-danger']"
    continoue_btn = By.XPATH,"//a[@class='btn btn-primary']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)

    def do_search(self,keyword):
        search = self.wait.until(EC.element_to_be_clickable(self.search_field))
        search.clear()
        search.send_keys(keyword)

    def click_search(self):
        self.wait.until(EC.element_to_be_clickable(self.serach_btn)).click()

    def show_productdetailpage(self):
        self.wait.until(EC.element_to_be_clickable(self.product_detail)).click()

    def do_wishlist(self):
        self.wait.until(EC.element_to_be_clickable(self.wishlist_btn)).click()

    def show_wishlisttable(self):
        self.wait.until(EC.element_to_be_clickable(self.wishlist_mainbtn)).click()

    def add_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_btn)).click()

    def add_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_btn)).click()

    def click_cont(self):
        self.wait.until(EC.element_to_be_clickable(self.continoue_btn)).click()

    def show_wishlistmessage(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.wishlist_success)).text
        except TimeoutException:
            return None

    def title_wishlisttable(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.title_wishlist)).text
        except TimeoutException:
            return None

    def get_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.cartorremove_success)).text
        except TimeoutException:
            return None