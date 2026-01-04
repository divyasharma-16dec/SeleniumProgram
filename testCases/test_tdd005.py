import time

import pytest
from selenium import webdriver

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage

from utilities.ReadProperties import ReadProperties
from utilities import XLUtils

import os

class TestMulogs():

    baseURL= ReadProperties.get_URL()
    path = os.path.abspath(os.curdir)+"\\testdata\\Opencart_LoginData.xlsx"

    def test_login_tdd(self,setup):
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[] #an empty list used to collect the result ('Pass'/'Fail') for each data row.


        self.driver = setup
        self.driver.get(self.baseURL)
        self.home = HomePage(self.driver)
        self.login = LoginPage(self.driver)

        for r in range(2, self.rows+1):
            self.home.click_accountlink()
            self.home.click_loginlink()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            self.login.click_loginemail(self.email)
            self.login.click_loginpassword(self.password)
            self.login.click_loginbutton()
            time.sleep(3)

            self.message = self.login.final_message()

            if self.exp == 'Valid':
                if self.message == True:
                    lst_status.append('Pass')
                    self.home.click_logoutlink()
                else:
                    self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"fail1.png")
                    lst_status.append('Fail')
            elif self.exp == 'Invalid':
                if self.message == False:
                    lst_status.append('Fail')
                    self.home.click_logoutlink()
                else:
                    self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"fail2.png")
                    lst_status.append('Pass')