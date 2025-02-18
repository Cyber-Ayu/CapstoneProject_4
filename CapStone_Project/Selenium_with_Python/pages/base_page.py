class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_element_selected(self, locator):
        return self.driver.find_element(*locator).is_selected()
