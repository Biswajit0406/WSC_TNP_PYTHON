import time
import pytest
from PageObject.loginpage import LoginPage
from Utility.Excel_data_Reader import utility
import os


testdata = utility.excel_data("C:/Users/KIIT/Documents/Demo test for python.xlsx", "Sheet1")

@pytest.mark.usefixtures("setup")
class TestLoginPage:


    def test_logo_visibility(self):
        # self.lp = LoginPage(setup)  # Use `setup`, which is the driver
        # assert self.lp.is_logo_visible()  # Use `self.lp`
        self.lp = LoginPage(self.driver)
        assert self.lp.is_logo_visible()


    @pytest.mark.parametrize(("username","password"),testdata)
    def test_login(self,username,password):
        self.lp = LoginPage(self.driver)
        self.lp.login(username,password)






