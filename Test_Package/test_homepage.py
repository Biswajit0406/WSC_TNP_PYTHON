import time
import pytest
from PageObject.loginpage import LoginPage
from Utility.Excel_data_Reader import utility
from PageObject.homepage import homepage
from PageObject.homepage import homepage



@pytest.mark.usefixtures("setup")
class Test_homepagePage:

    username = "tester"
    password = "tester@admin"

    def test_homepage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login(self.username,self.password)
        self.hp=homepage(self.driver)
        self.hp.home_portion()
        self.hp.scroll_to_SLCM()
        self.hp.click_SLCM()
