import pytest
from selenium import webdriver

loginpage_url = "https://wscdemo.eduleadonline.com"

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Specify the browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser,request):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(loginpage_url)
    request.cls.driver = driver

    yield driver  # Yield instead of return to ensure cleanup

    driver.quit()  # Close browser after tests
