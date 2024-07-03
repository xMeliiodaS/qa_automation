from selenium.webdriver.common.by import By

from logic.base_page import BasePage


class PracticeTestLoginPage(BasePage):
    # XPATH login section - locator
    USER_NAME_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    SUBMIT_BUTTON = '//button[@id="submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._submit_input = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

        # init_page()

    # # Another popular way
    # def init_page(self):
    #     self._user_name_input = self.find_element(By.XPATH, self.USER_NAME_INPUT)
    #     self._password_input = self.find_element(By.XPATH, self.PASSWORD_NAME_INPUT)
    #     self._submit_input = self.find_element(By.XPATH, self.SUBMIT_BUTTON)

    def fill_user_name_input(self, username):
        self._user_name_input.clear()
        self._user_name_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)

    def click_submit_button(self):
        self._submit_input.click()

    def login_flow(self, username, password):
        self.fill_user_name_input(username)
        self.fill_password_input(password)
        self.click_submit_button()
