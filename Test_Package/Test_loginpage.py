import time
import pytest
from PageObject.loginpage import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginPage:



    def test_logo_visibility(self):
        # self.lp = LoginPage(setup)  # Use `setup`, which is the driver
        # assert self.lp.is_logo_visible()  # Use `self.lp`
        self.lp = LoginPage(self.driver)
        assert self.lp.is_logo_visible()




