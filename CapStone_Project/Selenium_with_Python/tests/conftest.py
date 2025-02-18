import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()  # Update path if necessary
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/")
    yield driver
    driver.quit()
