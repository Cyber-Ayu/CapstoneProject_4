from pages.checkboxes_page import CheckboxesPage

def test_checkboxes(setup):
    driver = setup
    checkbox_page = CheckboxesPage(driver)

    # Navigate to Checkboxes page
    checkbox_page.navigate_to_checkboxes()

    # Verify the header
    assert checkbox_page.verify_checkbox_page_header() == "Checkboxes"

    # Validate checkbox states
    assert not checkbox_page.is_checkbox1_selected(), "Checkbox 1 should not be checked"
    assert checkbox_page.is_checkbox2_selected(), "Checkbox 2 should be checked"
