from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class ChallengingDomPage(BasePage):
    FIRST_BUTTON = '//a[@class="button"]'
    SECOND_BUTTON = '//a[@class="button alert"]'
    THIRD_BUTTON = '//a[@class="button success"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._first_button = self._driver.find_element(By.XPATH, self.FIRST_BUTTON)
        self._second_button = self._driver.find_element(By.XPATH, self.SECOND_BUTTON)
        self._third_button = self._driver.find_element(By.XPATH, self.THIRD_BUTTON)

    def click_on_first_button(self):
        self._first_button.click()

    def click_on_first_button(self):
        self._first_button.click()

    def click_on_first_button(self):
        self._first_button.click()
