import pytest
import os
import logging
from pages.home_page import HomePage
from pages.file_upload_page import FileUploadPage

logger = logging.getLogger(__name__)

def test_file_upload(driver, base_url):
    """Test to verify file upload functionality."""
    home = HomePage(driver)
    file_upload = FileUploadPage(driver)

    try:
        # Navigate to home page
        home.navigate_to(base_url)
        title = home.get_title()
        assert title == "The Internet", f"Expected title 'The Internet', but got {title}"

        # Click File Upload link and verify header
        home.click_file_upload()
        header_text = file_upload.get_header_text()
        assert header_text == "File Uploader", f"Expected header 'File Uploader', but got {header_text}"

        # Define file path and upload file
        file_path = os.path.join(os.getcwd(), "test_file.txt")
        file_upload.upload_file(file_path)

        # Verify successful upload
        success_message = file_upload.get_success_message()
        assert success_message == "File Uploaded!", f"Expected success message 'File Uploaded!', but got {success_message}"

        logger.info("File upload test passed successfully.")

    except AssertionError as e:
        logger.error(f"Test failed: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e