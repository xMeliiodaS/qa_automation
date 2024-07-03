from selenium.webdriver.common.by import By


class PracticeTestLoginPage:
    # XPATH login section - locator
    USER_NAME_INPUT = '//input[@id="username"]'
    PASSWORD_NAME_INPUT = '//input[@id="password"]'
    SUBMIT_BUTTON = '//button[id="submit"]'

    def __init__(self, driver):
        self._driver = driver
        self._user_name_input = self.find_element(By.ID, self.USER_NAME_INPUT)
        self._password_input = self.find_element(By.ID, self.PASSWORD_NAME_INPUT)
        self._submit_input = self.find_element(By.ID, self.SUBMIT_BUTTON)
