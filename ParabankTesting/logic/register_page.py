from selenium.webdriver.common.by import By
from logic.base_page_app import BasePage
from selenium import common as c


class RegisterPage(BasePage):
    USER_NAME_INPUT = '//input[@id="customer.firstName"]'
    PASSWORD_INPUT = '//input[@id="customer.lastName"]'
    ADDRESS_INPUT = '//input[@id="customer.address.street"]'
    CITY_INPUT = '//input[@id="customer.address.city"]'
    STATE_INPUT = '//input[@id="customer.address.state"]'
    ZIP_CODE_INPUT = '//input[@id="customer.address.zipCode"]'
    PHONE_INPUT = '//input[@id="customer.phoneNumber"]'
    SSN_INPUT = '//input[@id="customer.phoneNumber"]'
    USERNAME_INPUT = '//input[@id="customer.username"]'
    PASSWORD_INPUT = '//input[@id="customer.password"]'
    CONFIRM_INPUT = '//input[@id="repeatedPassword"]'
    REGISTER_BUTTON = '//input[@value="Register"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._submit_button = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def fill_user_name_input(self, user):
        self._user_name_input.send_key(user)


    def click_on_submit_button(self):
        self._submit_button.click()
