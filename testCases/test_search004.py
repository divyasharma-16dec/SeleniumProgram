import os.path

import pytest
from selenium import webdriver
from pageObjects.SearchPage import SearchPage
from utilities.ReadProperties import ReadProperties

''' 
✔ Search products by name
✔ Verify results contain relevant products
✔ Verify pagination if available
✔ Verify category filters
✔ Sort by price/name/rating
'''

class TestSearch():
    baseURL = ReadProperties.get_URL()

    @pytest.fixture()
    def setup_search(self,setup):
        driver = setup
        driver.get(self.baseURL)

        search = SearchPage(driver)
        return driver, search
    @pytest.mark.smoke
    def test_validsearch(self,setup_search):
        driver, search = setup_search
        search.click_searchfield("mac")
        search.click_searchbutton()


        title = search.show_producttitle()
        print("Mac keyword")
        for protitle in title:
            print("title = ",protitle)

        assert len(title)>0

        if search.show_listbutton():
            assert search.show_listbutton()
        else:
            assert False,"There is no product that matches the search criteria."

    def test_invalidsearch(self,setup_search):
        driver, search = setup_search
        search.click_searchfield("test")
        search.click_searchbutton()

        if search.show_noproductmessage():
            assert search.show_noproductmessage()
        else:
            assert False, "Item appeared."

    '''
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
            assert False,"Notadded"

        self.search.click_shoppingcart()
        message1 = self.search.get_messageofshoppingcart()

        if "not in stock" in message1:
            print("Products marked with *** are not available in the desired quantity or not in stock!")
            assert True
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+ "Valid.png")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+ "Empty.png")
            assert False,"Empty"
            
            '''


