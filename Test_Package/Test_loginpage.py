import time
import pytest
from PageObject.loginpage import LoginPage
from Utility.Excel_data_Reader import utility
from PageObject.homepage import homepage

# from Utility.CustomLogger import CustomLogger


testdata = utility.excel_data("C:/Users/KIIT/Documents/Demo test for python.xlsx", "Sheet1")
# logger = CustomLogger.logger_message()

@pytest.mark.usefixtures("setup")
class TestLoginPage:




    def test_logo_visibility(self):
        # self.lp = LoginPage(setup)  # Use `setup`, which is the driver
        # assert self.lp.is_logo_visible()  # Use `self.lp`
        self.lp = LoginPage(self.driver)
        assert self.lp.is_logo_visible()
        # logger.info("Test case passed")



    @pytest.mark.parametrize(("username","password"),testdata)
    def test_login(self,username,password):
        self.lp = LoginPage(self.driver)
        self.lp.login(username,password)
        self.hp=homepage(self.driver)
        self.hp.cry()





