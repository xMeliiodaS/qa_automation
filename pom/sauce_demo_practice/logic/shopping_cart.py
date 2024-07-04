from selenium.webdriver.common.by import By
from sauce_demo_practice.infra.base_page import BasePage


class ShoppingCart(BasePage):
    CART_BUTTON = '//a[@class="shopping_cart_link"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)

    def click_on_cart_button(self):
        self._cart_button.click()
