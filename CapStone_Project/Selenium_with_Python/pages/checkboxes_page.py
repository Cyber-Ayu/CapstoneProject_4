from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxesPage(BasePage):
    CHECKBOX_LINK = (By.LINK_TEXT, "Checkboxes")
    CHECKBOX_HEADER = (By.TAG_NAME, "h3")
    CHECKBOX1 = (By.XPATH, "//input[1]")
    CHECKBOX2 = (By.XPATH, "//input[2]")

    def navigate_to_checkboxes(self):
        self.click_element(self.CHECKBOX_LINK)

    def verify_checkbox_page_header(self):
        return self.get_element_text(self.CHECKBOX_HEADER)

    def is_checkbox1_selected(self):
        return self.is_element_selected(self.CHECKBOX1)

    def is_checkbox2_selected(self):
        return self.is_element_selected(self.CHECKBOX2)
