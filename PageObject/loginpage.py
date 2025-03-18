from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.BASEpage import Base

class LoginPage(Base):
    def __init__(self,driver):
        super().__init__(driver)
       


    # Web Elements (Using Locators)
    LOGO = (By.XPATH, "//section[@class='for-login']//div[@class='page-card-head']")
    USERNAME_FIELD = (By.XPATH, "//input[@id='login_email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='login_password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    SIGNUP_LOGIN = (By.XPATH, "//a[normalize-space()='Have an account? Login']")
    FORGOT_PASSWORD = (By.XPATH, "//a[normalize-space()='Forgot Password?']")
    FORGOT_EMAIL = (By.XPATH, "//input[@id='forgot_email']")
    RESET_PASSWORD = (By.XPATH, "//button[normalize-space()='Reset Password']")
    BACK_TO_LOGIN = (By.XPATH, "(//p[@class='text-center sign-up-message'])[2]")
    SIGNUP_BUTTON = (By.XPATH, "//a[normalize-space()='Sign up']")
    SIGNUP_NAME = (By.XPATH, "//input[@id='signup_fullname']")
    SIGNUP_EMAIL = (By.XPATH, "//input[@id='signup_email']")
    ALREADY_REGISTERED = (By.XPATH, "//button[normalize-space()='Already Registered']")
    DIALOG_BOX = (By.CSS_SELECTOR, "div[role='dialog']")
    SUCCESS_BUTTON = (By.XPATH, "//button[normalize-space()='Success']")
    VALID_EMAIL_PASSWORD = (By.XPATH, "//button[normalize-space()='Valid email and name required']")
    FORGOT_DIALOG_BOX = (By.XPATH, "//button[@aria-label='Close']")
    SIGNUP_DIALOG_BOX = (By.XPATH, "//button[@aria-label='Close'])[1]")

    # Action Methods
    def is_logo_visible(self):
        logo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((self.LOGO)))
        return logo.is_displayed()

    def login(self,username,password):
        self.send_keys(LoginPage.USERNAME_FIELD, username)
        self.send_keys(LoginPage.PASSWORD_FIELD, password)
        self.click(LoginPage.LOGIN_BUTTON)

