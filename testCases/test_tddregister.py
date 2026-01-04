import os
import pytest
from selenium import webdriver

from pageObjects.TddRegisterPage import TddRegisterPage
from pageObjects.HomePage import HomePage

from utilities.RandomString import RandomData

from utilities.ReadProperties import ReadProperties

from utilities import XLUtils

class TestRegisterTDD:
    baseURL = ReadProperties.get_URL()
    path = os.path.abspath(os.curdir) + "\\testData\\"+ "RegisterData11.xlsx"
    @pytest.fixture()
    def setup_register(self,setup):
        driver = setup
        driver.get(self.baseURL)

        register = TddRegisterPage(driver)
        home = HomePage(driver)

        home.click_accountlink()
        home.click_registerlink()

        return driver, register, home

    def test_register_tdd(self,setup_register):
        driver, register, home = setup_register

        rows = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status=[] #collect result of each row

        for r in range(2, rows+1):
            fn = XLUtils.readData(self.path,"Sheet1",r,2) or ""
            ln = XLUtils.readData(self.path,"Sheet1",r,3) or ""
            email = XLUtils.readData(self.path,"Sheet1",r,4) or ""
            telephone = XLUtils.readData(self.path,"Sheet1",r,5) or ""
            pw = XLUtils.readData(self.path,"Sheet1",r,6) or ""
            cpw = XLUtils.readData(self.path,"Sheet1",r,7) or ""
            exp = XLUtils.readData(self.path,"Sheet1",r,8)
            register = TddRegisterPage(driver)

            register.register_elements(fn,ln,email,telephone,pw,cpw)
            message = register.getconfirmationmessage()

            if exp == "Pass":
                if message == True:
                    lst_status.append('valid')
                    HomePage(driver).click_logoutlink()
                else:
                    lst_status.append('Fail')
            elif exp == "Fail":
                if message == False:
                    lst_status.append('invalid')
                else:
                    lst_status.append('valid')

            driver.get(self.baseURL)
            home = HomePage(driver)
            home.click_accountlink()
            home.click_registerlink()




