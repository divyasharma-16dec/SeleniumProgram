import time

from pageObjects.RegisterPage import RegisterPage
from pageObjects.HomePage import HomePage

import os

from utilities.ReadProperties import ReadProperties
'''
1. Conftest: function -- setup
2. register page: class -- RegisterPage & fuctions -- enterFirtName , ....
    parametrer -- driver
3. home page: class -- HomePage & functions -- 
    parameter -- setup
'''

class TestRegister:
    baseURL= ReadProperties.get_URL()

    def test_doregister(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = HomePage(self.driver)
        self.hp.click_accountlink()
        self.hp.click_registerlink()

        self.register = RegisterPage(self.driver)
        self.register.enter_firstname()
        self.register.enter_lastname()
        self.register.enter_emailid()
        self.register.enter_telephone()
        self.register.enter_password()
        self.register.enter_confirmpassword()
        self.register.select_newsletters()
        self.register.click_privacypolicy()
        self.register.click_registersubmit()
        if self.register.getconfirmationmessage():
            print("Register done")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_register001.png")
            print("Register is not done.")
            assert False

        self.hp.click_accountlink()
        time.sleep(2)
        self.hp.click_logoutlink()













