
from datetime import datetime

import pytest
from selenium import webdriver
import os

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome / firefox / edge"
    )
'''
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = Options()
        options.add_argument("--headless")               # REQUIRED FOR CI
        options.add_argument("--no-sandbox")             # REQUIRED FOR CI
        options.add_argument("--disable-dev-shm-usage")  # REQUIRED FOR CI

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

'''
#### HTML Report ####

# It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'TutorialsNinja'
    config._metadata['Module Name'] = 'Register & Login'
    config._metadata['Tester'] = 'Divya Sharma'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
'''