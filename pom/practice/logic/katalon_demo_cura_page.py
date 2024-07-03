from selenium.webdriver.common.by import By

from practice.infra.base_page import BasePage


class KatalonDemoCuraPage(BasePage):
    MAKE_APPOINTMENT_BUTTON = '//a[@id="btn-make-appointment"]'
    MENU_BUTTON = '//a[@id="menu-toggle"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._make_appointment_button = self._driver.find_element(By.XPATH, self.MAKE_APPOINTMENT_BUTTON)
        self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)

    def click_on_make_appointment_button(self):
        self._make_appointment_button.click()

    def click_on_meny_button(self):
        self._menu_button.click()