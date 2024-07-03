from selenium import webdriver
from selenium.webdriver.common.by import By


class PracticeTestLoginPage:
    # XPATH login section - locator
    USER_NAME_INPUT = '//input[@id="username"]'
    PASSWORD_NAME_INPUT = '//input[@id="password"]'
    SUBMIT_BUTTON = '//button[id="submit"]'

    def __init__(self, driver):
        self._driver = webdriver.Chrome()
        # self._driver = driver
        self._user_name_input = self.find_element(By.XPATH, self.USER_NAME_INPUT)
        self._password_input = self.find_element(By.XPATH, self.PASSWORD_NAME_INPUT)
        self._submit_input = self.find_element(By.XPATH, self.SUBMIT_BUTTON)

    def fill_user_name_input(self, username):
        self._user_name_input.send_keys(username)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_submit_button(self):
        self._submit_input.click()


