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
    def send_keys(self,locator,value):
        element = self.get_element(locator)
        element.send_keys(value)


    def visibility(self,locator):
        element = self.get_element(locator)
        return element.is_displayed()

    def get_element(self, locator):
        element = None
        if locator.__contains__("_id"):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        elif locator.__contains__("//"):
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element


