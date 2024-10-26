import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
import sys
import selenium

@pytest.fixture
def driver():
    # Setup
    service = Service(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()

def pytest_html_report_title(report):
    report.title = "Sauce Demo Test Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                driver = item.funcargs['driver']
                screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                driver.save_screenshot(f'reports/{screenshot_name}')
                if screenshot_name:
                    html = f'<div><img src="{screenshot_name}" alt="screenshot" style="width:600px;height:300px;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
        report.extra = extra

def pytest_configure(config):
    config._metadata = {
        "Tester": "Your Name",
        "Project": "Sauce Demo",
        "Test Environment": "QA",
        "Browser": "Edge",
        "Platform": "Windows",
        "Python Version": sys.version,
        "Selenium Version": selenium.__version__
    }

def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.pop()

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{getattr(report, 'description', '')}</td>")
    cells.pop()