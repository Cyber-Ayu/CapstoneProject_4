import os
from selenium.webdriver.common.by import By


class FileUploadPage:
    """Page Object for File Upload Page."""

    HEADER = (By.TAG_NAME, "h3")
    CHOOSE_FILE = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOAD_SUCCESS = (By.TAG_NAME, "h3")

    def __init__(self, driver):
        self.driver = driver

    def get_header_text(self):
        return self.driver.find_element(*self.HEADER).text

    def upload_file(self, file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("This is a test file for upload.")  # Ensure the file exists
        self.driver.find_element(*self.CHOOSE_FILE).send_keys(file_path)
        self.driver.find_element(*self.UPLOAD_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.UPLOAD_SUCCESS).text
