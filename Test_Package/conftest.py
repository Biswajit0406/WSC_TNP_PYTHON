import pytest
from selenium import webdriver
import logging
from Utility.CustomLogger import CustomLogger
import os


loginpage_url = "https://wscdemo.eduleadonline.com"
logger = CustomLogger.logger_message()
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Specify the browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser,request):
    global driver
    if browser == "chrome":
        logger.info("Initializing WebDriver...")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        logger.info("Initializing WebDriver...")
        driver = webdriver.Firefox()
    elif browser == "edge":
        logger.info("Initializing WebDriver...")
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(loginpage_url)
    request.cls.driver = driver

    yield driver  # Yield instead of return to ensure cleanup
    # Capture screenshot on failure
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_path)
        logger.error(f"Test Failed! Screenshot saved at: {screenshot_path}")

        # Attach screenshot to pytest-html report
        if hasattr(request.config, "_html"):
            extra = getattr(request.config, "_html").extras
            extra.append(pytest_html.extras.png(screenshot_path))

    driver.quit()
    logger.info("Test Completed. WebDriver closed.")


# Hook for attaching screenshot to pytest-html report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Enable pytest-html integration"""
    config._html = config.pluginmanager.getplugin("html")