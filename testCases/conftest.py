import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome / firefox / edge"
    )

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
