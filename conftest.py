import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()