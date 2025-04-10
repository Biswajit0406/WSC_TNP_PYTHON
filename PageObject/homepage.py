from selenium.webdriver.common.by import By
from Base.BASEpage import Base
class homepage(Base):

    T_N_P = (By.XPATH,  "//span[normalize-space()='Training and Placement']")
    slcm=(By.CSS_SELECTOR,"div[class='desk-sidebar-item standard-sidebar-item selected'] span[class='drop-icon show-in-edit-mode'] svg")
    def __init__(self,driver):
        super().__init__(driver)


    def cry(self):
        self.click(self.slcm)
        self.scroll_to_element(self.T_N_P)

        self.click(self.T_N_P)