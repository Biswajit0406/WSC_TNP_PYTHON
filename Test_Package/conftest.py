# import pytest
# from selenium import webdriver
# import logging
# from Utility.CustomLogger import CustomLogger
# import os
# from selenium.webdriver.chrome.options import Options
#
#
# loginpage_url = "https://wscdemo.eduleadonline.com"
# logger = CustomLogger.logger_message()
# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store",default="chrome",help="Specify the browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser, request):
#     global driver
#     options = Options()
#     options.add_argument("--headless")  # Run in background
#     options.add_argument("--disable-gpu")  # Improve performance on Windows
#
#     if browser == "chrome":
#         driver = webdriver.Chrome(options=options)
#     elif browser == "firefox":
#         from selenium.webdriver.firefox.options import Options as FirefoxOptions
#         options = FirefoxOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)
#     elif browser == "edge":
#         from selenium.webdriver.edge.options import Options as EdgeOptions
#         options = EdgeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Edge(options=options)
#     else:
#         raise ValueError("Unsupported browser")
#
#     driver.maximize_window()
#     driver.get(loginpage_url)
#     request.cls.driver = driver
#
#     yield driver  # Yield instead of return to ensure cleanup
#     # Capture screenshot on failure
#     if request.node.rep_call.failed:
#         a=0;
#         screenshot_dir = "Screenshot"
#         os.makedirs(screenshot_dir, exist_ok=True)  # Ensure directory exists
#         screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}+a++.png")
#         driver.save_screenshot(screenshot_path)
#         logger.error(f"Test Failed! Screenshot saved at: {screenshot_path}")
#
#         # Attach screenshot to pytest-html report
#         if hasattr(request.config, "_html"):
#             extra = getattr(request.config, "_html").extras
#             extra.append(pytest_html.extras.png(screenshot_path))
#
#     driver.quit()
#     logger.info("Test Completed. WebDriver closed.")
#
#
# # Hook for attaching screenshot to pytest-html report
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     setattr(item, "rep_" + report.when, report)
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     """Enable pytest-html integration"""
#     config._html = config.pluginmanager.getplugin("html")