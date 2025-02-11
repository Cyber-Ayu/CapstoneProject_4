import pytest
import logging
from pages.home_page import HomePage
from pages.checkboxes_page import CheckboxesPage

logger = logging.getLogger(__name__)

def test_checkboxes(driver, base_url):
    """Test to verify checkboxes page."""
    home = HomePage(driver)
    checkboxes = CheckboxesPage(driver)

    try:
        # Navigate to home page and verify title
        home.navigate_to(base_url)
        title = home.get_title()
        assert title == "The Internet", f"Expected title 'The Internet', but got {title}"

        # Click Checkboxes link and verify header
        home.click_checkboxes()
        header_text = checkboxes.get_header_text()
        assert header_text == "Checkboxes", f"Expected header 'Checkboxes', but got {header_text}"

        # Verify checkbox states: Checkbox 1 is NOT checked, Checkbox 2 is checked
        checkbox_states = checkboxes.get_checkbox_states()
        expected_states = [False, True]
        assert checkbox_states == expected_states, f"Unexpected checkbox states: {checkbox_states}, expected: {expected_states}"

        logger.info("Checkbox states verified successfully.")

    except AssertionError as e:
        logger.error(f"Test failed: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e