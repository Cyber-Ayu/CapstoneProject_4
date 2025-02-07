import pytest
from pages.home_page import HomePage
from pages.checkboxes_page import CheckboxesPage


def test_checkboxes(driver, base_url):
    """Test to verify checkboxes page."""
    home = HomePage(driver)
    checkboxes = CheckboxesPage(driver)

    # Navigate to home page and verify title
    home.navigate_to(base_url)
    assert home.get_title() == "The Internet"

    # Click Checkboxes link and verify header
    home.click_checkboxes()
    assert checkboxes.get_header_text() == "Checkboxes"

    # Verify checkbox states: Checkbox 1 is NOT checked, Checkbox 2 is checked
    checkbox_states = checkboxes.get_checkbox_states()
    assert checkbox_states == [
        False,
        True,
    ], f"Unexpected checkbox states: {checkbox_states}"
