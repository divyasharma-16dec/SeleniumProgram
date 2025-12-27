import pytest
from selenium import webdriver
from pageObjects.SearchPage import SearchPage
from utilities.ReadProperties import ReadProperties

class TestSearch():
    baseURL = ReadProperties.get_URL()

    def test_dosearch(self,setup):
        self.driver = setup

        self.driver.get(self.baseURL)
        self.search = SearchPage(self.driver)
        self.search.click_searchfield()
        self.search.click_searchbutton()
        self.search.select_product()
        self.search.addproduct_cart()
        message = self.search.get_successmessage()


        if "Success" in message:
            print("Add to cart successfull")
            assert True
        else:
            print("Not added")
            assert False

        self.search.click_shoppingcart()
        message1 = self.search.get_messageofshoppingcart()

        if "not in stock" in message1:
            print("Products marked with *** are not available in the desired quantity or not in stock!")
            assert True
        else:
            print("Empty")
            assert False

        self.driver.quit()

