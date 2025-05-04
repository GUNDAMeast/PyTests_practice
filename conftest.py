import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     choices=["chrome", "firefox"],
                     help="Choose your browser: ")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose your language: ")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        opts = ChromeOptions()
        opts.add_experimental_option("prefs", {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=opts)
    else:
        opts = FFOptions()
        opts.set_preference('intl.accept_languages', language)
        driver = webdriver.Firefox(options=opts)

    driver.implicitly_wait(5)
    yield driver
    print("quit browser…")
    driver.quit()
