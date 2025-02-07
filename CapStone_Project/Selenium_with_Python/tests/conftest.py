import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    """Base URL for the application."""
    return "http://the-internet.herokuapp.com/"
