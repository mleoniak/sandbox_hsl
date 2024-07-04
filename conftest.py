import pytest
from selenium import webdriver
from src.applications.ui.hsl_nyu_ui import HslNyuUI
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "NYU HSL Test Automation Report"


# fixture for tests
@pytest.fixture
def hsl_nyu_ui_app():
    #Headless browser
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()

    # 1. Prestep. Navigate to GithubAPP
    hslnyuui_app = HslNyuUI(browser=driver)
    hslnyuui_app.open()

    # generators in python
    yield hslnyuui_app

    # PostStep. Close the App
    hslnyuui_app.close()
