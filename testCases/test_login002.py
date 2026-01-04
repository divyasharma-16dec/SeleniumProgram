import time

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadProperties

import os

class TestLogin:

    baseURL = ReadProperties.get_URL()
    @pytest.fixture() #Runs before each test
    def setup_login(self,setup):
        driver = setup
        driver.get(self.baseURL)

        hp = HomePage(driver)
        hp.click_accountlink()
        hp.click_loginlink()

        login_p = LoginPage(driver)
        return hp, login_p


    def test_validlogin(self,setup_login):
        hp, login_p = setup_login
        login_p.login_elements("d55@yopmail.com","Test1234@")
        print("Testcases hasbeen done")

        assert login_p.show_loginmessage()

    def test_invaliddata(self,setup_login):
        hp, login_p = setup_login
        login_p.login_elements("gg@gg","hhh")
        assert login_p.invalid_message()

    def test_blankdata(self, setup_login):
        hp, login_p = setup_login
        login_p.login_elements(" ", " ")
        assert login_p.invalid_message()

    def test_gotohomepage(self,setup_login):
        hp, login_p = setup_login
        login_p.login_elements("d55@yopmail.com","Test1234@")
        hp.click_logout()

        assert login_p.logout_message()

    def test_session(self,setup):
        driver = setup
        driver.get(self.baseURL)

        hp = HomePage(driver)
        hp.click_accountlink()
        hp.click_loginlink()

        login_p = LoginPage(driver)

        login_p.login_elements("d55@yopmail.com","Test1234@")

        driver.delete_all_cookies()
        driver.refresh()
        hp.click_accountlink()
        hp.click_loginlink()

        assert "login" in driver.title






'''
        login_p.click_normalloginemail()
        login_p.click_normalloginpassword()
        login_p.click_loginbutton()

    def test_valid(self,setup_login):
        hp, 
        message = login_p.show_loginmessage()

        if message:
            print("User has been login successfully")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "invalid.png")
            assert False,"Not done"

    def test_invalidlogin(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        hp = HomePage(self.driver)
        hp.click_accountlink()
        hp.click_loginlink()
'''