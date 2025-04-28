import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")



@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test...")
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxProfile()
        options.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(firefox_profile=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    time.sleep(7)
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def product_link():
    return "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"

def second_product_link():
    return "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.fixture
def main_link():
    return "http://selenium1py.pythonanywhere.com/"
 

