import pytest
import os
from pages.home_page import HomePage
from pages.file_upload_page import FileUploadPage


def test_file_upload(driver, base_url):
    """Test to verify file upload functionality."""
    home = HomePage(driver)
    file_upload = FileUploadPage(driver)

    # Navigate to home page
    home.navigate_to(base_url)
    assert home.get_title() == "The Internet"

    # Click File Upload link and verify header
    home.click_file_upload()
    assert file_upload.get_header_text() == "File Uploader"

    # Define file path and upload file
    file_path = os.path.join(os.getcwd(), "test_file.txt")
    file_upload.upload_file(file_path)

    # Verify successful upload
    assert file_upload.get_success_message() == "File Uploaded!"
