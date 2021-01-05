import pytest
from selenium import webdriver
from pageObjects.loginpage import LoginPage
from Utilities.readProperty import ReadConfig

class Test_001_login:
    baseURL = ReadConfig.getAppURL()
    print (baseURL)
    username = ReadConfig.getuser()
    password = ReadConfig.getpass()

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(sef.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Nomus WiZ":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "WIRELESS ACCESS ROUTER":
            assert True
        else:
            assert False
