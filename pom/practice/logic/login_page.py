from selenium.webdriver.common.by import By
from practice.infra.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME_INPUT = '//input[@class="form-control" and @name="username"]'
    PASSWORD_INPUT = '//input[@class="form-control" and @name="password"]'
    LOGIN_BUTTON = '//button[@id="btn-login"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._submit_input = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
