from pages.file_upload_page import FileUploadPage
import os

def test_file_upload(setup):
    driver = setup
    file_upload_page = FileUploadPage(driver)

    # Navigate to File Upload page
    file_upload_page.navigate_to_file_upload()

    # Verify the header
    assert file_upload_page.verify_upload_page_header() == "File Uploader"

    # Upload file
    file_path = os.path.abspath("test_file.txt")
    file_upload_page.upload_file(file_path)

    # Verify upload success
    assert file_upload_page.get_upload_success_message() == "File Uploaded!"
