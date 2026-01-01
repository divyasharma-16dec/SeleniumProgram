import pytest
from selenium import webdriver

import os

from pageObjects.ShoppingCart import ShoppingCart
from pageObjects.ProductPage import ProductPage
from pageObjects.SearchPage import SearchPage
from utilities.ReadProperties import ReadProperties

class TestCart():

    baseURL = ReadProperties.get_URL()
    @pytest.fixture()
    def setup_cart(self,setup):
        driver = setup
        driver.get(self.baseURL)
        return driver

    def test_add_product_to_cart(self,setup_cart):
        driver = setup_cart
        search = SearchPage(driver)
        search.click_searchfield("mac")
        search.click_searchbutton()
        search.select_product()
        search.addproduct_cart()

        cart = ShoppingCart(driver)
        cart.open_cart()

        assert "iMac" in cart.get_product_name()

    def test_update_product_to_cart(self,setup_cart):
        driver= setup_cart
        search = SearchPage(driver)
        search.click_searchfield("mac")
        search.click_searchbutton()
        search.select_product()
        search.addproduct_cart()

        cart = ShoppingCart(driver)
        cart.open_cart()
        cart.update_quantity("3")

        assert cart.quantity_successmessage()

    @pytest.mark.smoke
    def test_update_product_to_cart(self,setup_cart):
        driver= setup_cart
        search = SearchPage(driver)
        search.click_searchfield("mac")
        search.click_searchbutton()
        search.select_product()
        search.addproduct_cart()

        cart = ShoppingCart(driver)
        cart.open_cart()
        cart.update_quantity("3")
        cart.remove_product()

        assert cart.open_cart()

    def test_empty(self,setup_cart):
        driver = setup_cart
        cart = ShoppingCart(driver)
        cart.open_cart()
        assert cart.open_cart()




