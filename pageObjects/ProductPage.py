import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ProductPage():
    navigation_product2 = By.LINK_TEXT, "Components"
    product2_subpro = By.LINK_TEXT, "Monitors (2)"
    sortby_filter = By.ID, "input-sort"
    show_filter = By.ID, "input-limit"
    product_1 = By.XPATH, "//img[contains(@title,'Samsung SyncMaster 941BW')]"
    product_1wishlist = By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]"
    login_confirmationmessage = By.XPATH,"//*[@id='product-product']/div[1]"
    product_name = By.XPATH, "//*[@id='content']//h1[1]"
    wishlist_message = By.XPATH,"//div[@class='alert alert-success alert-dismissible']"

    def __init__(self,driver):
        self.driver = driver

    def click_nav2(self):
        self.driver.find_element(*self.navigation_product2).click()

    def click_navsubpro2(self):
        self.driver.find_element(*self.product2_subpro).click()

    def click_sortbyfilter(self):
        Select(self.driver.find_element(*self.sortby_filter)).select_by_visible_text("Price (Low > High)")

    def click_showfilter(self):
        Select(self.driver.find_element(*self.show_filter)).select_by_visible_text("100")

    def click_product1(self):
        self.driver.find_element(*self.product_1).click()

    def click_wishlist(self):
        self.driver.find_element(*self.product_1wishlist).click()

    def get_productname(self):
        return self.driver.find_element(*self.product_name).text


    def show_wishlistmessage(self):
        return self.driver.find_element(*self.wishlist_message).text

