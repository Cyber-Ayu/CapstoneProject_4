from selenium.webdriver.common.by import By


class HomePage:
    """Page Object for Home Page."""

    CHECKBOXES_LINK = (By.LINK_TEXT, "Checkboxes")
    FILE_UPLOAD_LINK = (By.LINK_TEXT, "File Upload")

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click_checkboxes(self):
        self.driver.find_element(*self.CHECKBOXES_LINK).click()

    def click_file_upload(self):
        self.driver.find_element(*self.FILE_UPLOAD_LINK).click()
