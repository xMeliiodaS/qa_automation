from selenium.webdriver.common.by import By


class BasePage:
    HOME_HEADER = '//a[text()="Home"]'

    def __init__(self, driver):
        self._driver = driver
        self._home_header_button = self._driver.find_element(By.XPATH, self.HOME_HEADER)

    def click_on_home_header_button(self):
        self._home_header_button.click()
