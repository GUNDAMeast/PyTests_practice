import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose your language: ")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    print("\nquit browser..")
    driver.quit()
