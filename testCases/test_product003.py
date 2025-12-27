import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage

class TestProduct():
    baseURL = "https://tutorialsninja.com/demo/"

    def test_productdetail(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        product_detail = ProductPage(self.driver)
        product_detail.click_nav2()
        product_detail.click_navsubpro2()
        product_detail.click_sortbyfilter()
        product_detail.click_showfilter()
        product_detail.click_product1()
        product_detail.click_wishlist()

        productname = product_detail.get_productname()
        print(productname)

        message = product_detail.show_wishlistmessage()
        print(message)

        if "You must login or create an account to save " in message and productname:
            print(f" You must login or create an account to save {productname} to your wish list!")
        else:
            print("nothing")
