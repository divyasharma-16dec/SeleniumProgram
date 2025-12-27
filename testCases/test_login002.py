import time

from pageObjects.HomePage import HomePage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.LoginPage import LoginPage
from utilities.ReadProperties import ReadProperties

class TestLogin():

    baseURL = ReadProperties.get_URL()

    def test_dologin(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        hp = HomePage(self.driver)
        hp.click_accountlink()
        hp.click_loginlink()

        login_p = LoginPage(self.driver)
        login_p.click_loginemail()
        login_p.click_loginpassword()
        login_p.click_loginbutton()

        message = login_p.show_loginmessage()

        if "Edit your account information" in message:
            print("Login suceessfull.")
        else:
            print("Not Login")
