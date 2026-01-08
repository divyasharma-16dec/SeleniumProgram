import pytest

from pageObjects.WishList import WishList
from utilities.ReadProperties import ReadProperties

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage

import os

class TestWishlist:

    base_url = ReadProperties.get_URL()

    @pytest.fixture()
    def setup_wishlist(self,setup):
        driver = setup
        driver.get(self.base_url)
        home = HomePage(driver)
        home.click_accountlink()
        home.click_loginlink()

        login = LoginPage(driver)
        login.login_elements("d55@yopmail.com","Test1234@")

        main = WishList(driver)
        main.do_search("mac")
        main.click_search()

        return driver,home,login,main

    @pytest.mark.smoke
    def test_wishlist(self,setup_wishlist):
        driver,home,login,main = setup_wishlist

        main.show_productdetailpage()
        main.do_wishlist()

        message = main.show_wishlistmessage()

        assert "wish list" in message

    @pytest.mark.smoke
    def test_wishlistmainpage(self,setup_wishlist):
        driver,home,login,main = setup_wishlist

        main.show_productdetailpage()
        main.do_wishlist()
        main.show_wishlisttable()

        title = main.title_wishlisttable()
        assert "My Wish List" in title

    @pytest.mark.smoke
    def test_cart(self,setup_wishlist):
        driver,home,login,main = setup_wishlist

        main.show_productdetailpage()
        main.do_wishlist()
        main.show_wishlisttable()

        main.add_cart()
        cart_message = main.get_message()
        assert "Success: You have added iMac to your shopping cart!" in cart_message

    @pytest.mark.smoke
    def test_deleteitem(self,setup_wishlist):
        driver,home,login,main = setup_wishlist

        main.show_productdetailpage()
        main.do_wishlist()
        main.show_wishlisttable()
        main.add_delete()
        delete_message = main.get_message()
        assert "Success: You have modified your wish list!" in delete_message





