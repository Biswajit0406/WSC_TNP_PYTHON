from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class Base:
    def __init__(self,driver):
        self.driver = driver



    def click(self,locator):
        element = self.get_element(locator)
        element.click()
    # def send_keys(self, locator, value):
    #     element = self.get_element(locator)
    #     element.send_keys(value)
    def get_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Element not found: {locator} — {e}")
            return None

    def send_keys(self, locator, value):
        element = self.get_element(locator)
        if element:
            element.clear()
            element.send_keys(value)
        else:
            raise Exception(f"Could not find element to send keys: {locator}")


    def visibility(self,locator):
        element = self.get_element(locator)
        return element.is_displayed()

    # def get_element(self, locator):
    #     element = None
    #     if locator.__contains__("_id"):
    #         element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.ID,locator))
    #     elif locator.__contains__("//"):
    #         element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH,locator))
    #     return element



    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))



    def select_by_text(self, locator, text):
        element = self.get_element(locator)
        Select(element).select_by_visible_text(text)
