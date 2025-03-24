
import pytest
from selenium import webdriver
import logging
from Utility.CustomLogger import CustomLogger
import os
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pytest_html import extras  # Import for attaching screenshots
from Utility.Configreader import Configurations

loginpage_url = Configurations.get_url()
logger = CustomLogger.logger_message()

# Dictionary to keep track of screenshot counts
screenshot_counts = {}

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser, request):
    global driver

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        from selenium.webdriver.edge.options import Options as EdgeOptions
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(loginpage_url)
    request.cls.driver = driver

    yield driver

    if request.node.rep_call.failed:
        screenshot_dir = "Screenshot"
        os.makedirs(screenshot_dir, exist_ok=True)

        test_name = request.node.name

        # Increment screenshot count for this test case
        if test_name in screenshot_counts:
            screenshot_counts[test_name] += 1
        else:
            screenshot_counts[test_name] = 1

        # Append counter to filename
        screenshot_name = f"{test_name}_{screenshot_counts[test_name]}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        driver.save_screenshot(screenshot_path)
        logger.error(f"Test Failed! Screenshot saved at: {screenshot_path}")

        # Attach screenshot to pytest-html report
        if hasattr(request.config, "_html"):
            extra = getattr(request.config, "_html").extras
            extra.append(extras.png(screenshot_path))

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