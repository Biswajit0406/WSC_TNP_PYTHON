import pytest
from selenium.webdriver.common.by import By
from Base.BASEpage import Base
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures('setup')
class homepage(Base):

    T_N_P = "//span[contains(@class,'sidebar-item-label')][normalize-space()='Training and Placement']"
    slcm = "/html/body/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div[2]/div[40]/div[1]/div/span/svg"
    dashboard = "//span[normalize-space()='Dashboard WSC']"
    Portion = "//div[@class='col-lg-2 layout-side-section']"
    buying="//span[normalize-space()='Buying']"

    def __init__(self, driver):
        super().__init__(driver)

    def home_portion(self):
        self.driver.find_element(By.XPATH,self.buying)
        a = ActionChains(self.driver)
        a.move_to_element(self.buying)

    def scroll_to_SLCM(self):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth',block: 'center'})", self.slcm)

    def click_SLCM(self):
        self.click(self.slcm)





    # def cry(self):
    #     # Step 1: Locate the SLCM SVG element
    #
    #     # Step 2: Scroll to SLCM
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", Portion)
    #
    #     # Step 3: Click using JavaScript
    #     s
    #     SLCM = self.driver.find_element(By.XPATH,
    #                                "//div[@item-name='SLCM']//span[@class='drop-icon show-in-edit-mode']//*[name()='svg']")
    #
    #     # Step 2: Scroll to SLCM
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", SLCM)
    #
    #     # Step 3: Click using JavaScript
    #     self.driver.execute_script("arguments[0].click();", SLCM)
    #
    #     # Optional: Wait for the dropdown to load (you can adjust time or use WebDriverWait)
    #     import time
    #     time.sleep(1)
    #
    #     # Step 4: Click on 'Training and Placement'
    #     tnp = self.driver.find_element(By.XPATH, "//span[contains(@class,'sidebar-item-label')][normalize-space()='Training and Placement']")
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", tnp)
    #     self.driver.execute_script("arguments[0].click();", tnp)
