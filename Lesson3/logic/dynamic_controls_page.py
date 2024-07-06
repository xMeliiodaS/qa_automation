from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class DynamicControlsPage(BasePage):
    CHECKBOX = '//input[@type="checkbox"]'
    ADD_REMOVE_BUTTON = '//button[@onclick="swapCheckbox()"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._checkbox = self._driver.find_element(By.XPATH, self.CHECKBOX)

    def click_on_checkbox(self):
        self._checkbox.click()

    def check_buttons_text(self):
        button_text = self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).text
        if button_text == "Remove":
            return "Remove"
        else:
            return "Add"

    def click_on_remove_button(self):
        if self.check_buttons_text() == "Remove":
            self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_REMOVE_BUTTON)))

    def click_on_add_button(self):
        if self.check_buttons_text() == "Add":
            self._driver.find_element(By.XPATH, self.ADD_REMOVE_BUTTON).click()
        WebDriverWait(self._driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_REMOVE_BUTTON)))
        # Refresh the checkbox element after the button click
        self._checkbox = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.CHECKBOX)))

    def click_on_checkbox_forced(self):
        self.click_on_add_button()
        self.click_on_checkbox()
