import pytest
from selenium import webdriver
from src.applications.ui.hsl_nyu_ui import HslNyuUI

# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "NYU HSL Test Automation Report"

# fixture for tests
@pytest.fixture
def hsl_nyu_ui_app():
    pass
    driver = webdriver.Firefox()

    #1. Prestep. Navigate to GithubAPP
    hslnyuui_app = HslNyuUI(browser=driver)
    hslnyuui_app.open()
    
    # generators in python
    yield hslnyuui_app

    # PostStep. Close the App
    hslnyuui_app.close() 
    
