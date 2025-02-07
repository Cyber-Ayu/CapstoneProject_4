from selenium.webdriver.common.by import By


class CheckboxesPage:
    """Page Object for Checkboxes Page."""

    HEADER = (By.TAG_NAME, "h3")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def get_header_text(self):
        return self.driver.find_element(*self.HEADER).text

    def get_checkbox_states(self):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return [
            checkbox.is_selected() for checkbox in checkboxes
        ]  # Returns [False, True]
