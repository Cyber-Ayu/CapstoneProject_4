from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FileUploadPage(BasePage):
    FILE_UPLOAD_LINK = (By.LINK_TEXT, "File Upload")
    FILE_UPLOAD_HEADER = (By.TAG_NAME, "h3")
    CHOOSE_FILE = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOAD_SUCCESS_TEXT = (By.TAG_NAME, "h3")

    def navigate_to_file_upload(self):
        self.click_element(self.FILE_UPLOAD_LINK)

    def verify_upload_page_header(self):
        return self.get_element_text(self.FILE_UPLOAD_HEADER)

    def upload_file(self, file_path):
        self.driver.find_element(*self.CHOOSE_FILE).send_keys(file_path)
        self.click_element(self.UPLOAD_BUTTON)

    def get_upload_success_message(self):
        return self.get_element_text(self.UPLOAD_SUCCESS_TEXT)
