from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base:
    def __init__(self,driver):
        self.driver = driver



    def click(self,locator):
        element = self.get_element(locator)
        element.click()
    def send_keys(self, locator, value):
        element = self.get_element(locator)
        if element:
            element.send_keys(value)
        else:
            raise Exception(f"Element with locator {locator} not found. Cannot send keys.")


    def visibility(self,locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def get_element(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except:
            print(f"Element with locator {locator} not found.")
            return None


