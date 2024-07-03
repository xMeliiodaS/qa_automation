from selenium.webdriver.common.by import By
from sauce_demo_practice.logic.base_page_app import BasePageApp


class InventoryPage(BasePageApp):
    ADD_TO_CART_BUTTON_ONE = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BUTTON_TWO = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_BUTTON_THREE = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    ITEM_NAME_BUTTON = '//div[contains(text(), "Sauce Labs Backpack")]'
    IMAGE_ITEM_CLICK = '//a[@id="item_4_img_link"]//img'
    CART_BUTTON = '//a[@class="shopping_cart_link"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button_one = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_ONE)
        self._add_to_cart_button_two = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_TWO)
        self._add_to_cart_button_three = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_THREE)
        self._item_name_button = self._driver.find_element(By.XPATH, self.ITEM_NAME_BUTTON)
        self._image_item_click = self._driver.find_element(By.XPATH, self.IMAGE_ITEM_CLICK)
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)

    def click_on_item_name_button(self):
        self._item_name_button.click()
        self._drive.back()

    def click_on_item_image(self):
        self._image_item_click.click()
        self._drive.back()

    def add_item_to_cart_one(self):
        self._add_to_cart_button_one.click()

    def add_item_to_cart_two(self):
        self._add_to_cart_button_two.click()

    def add_item_to_cart_three(self):
        self._add_to_cart_button_three.click()

    def add_three_items_to_cart(self):
        self.add_item_to_cart_one()
        self.add_item_to_cart_two()
        self.add_item_to_cart_three()



