import pytest
from selenium import webdriver

from src.applications.ui.hsl_nyu_ui import HslNyuUI
from testmo_reporter import create_test_run, add_test_result

from selenium.webdriver import FirefoxOptions as Options


# hook for pytest plugin
def pytest_html_report_title(report):
    report.title = "NYU HSL Test Automation Report"


# fixture for tests
@pytest.fixture
def hsl_nyu_ui_app():
    # #Headless browser
    options = Options()
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


# Testmo configuration


@pytest.fixture(scope="session")
def testmo_run():
    project_id = "your_project_id"
    run = create_test_run(project_id, "Automated Test Run")
    return run["id"]


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Mapping pytest outcomes to Testmo statuses
    status_mapping = {"passed": "success", "failed": "failure", "skipped": "skipped"}

    testmo_case_id = item.get_closest_marker("testmo_case_id")
    if testmo_case_id:
        case_id = testmo_case_id.args[0]
        status = status_mapping.get(result.outcome)
        comment = result.longreprtext if result.failed else ""
        run_id = item.config._testmo_run_id
        add_test_result(run_id, case_id, status, comment)


def pytest_configure(config):
    config._testmo_run_id = config.getoption("--testmo-run-id")


def pytest_addoption(parser):
    parser.addoption("--testmo-run-id", action="store")
