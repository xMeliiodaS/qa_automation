from selenium.webdriver.common.by import By
from sauce_demo_practice.infra.base_page import BasePage


class BasePageApp(BasePage):
    MAIN_MENU_BUTTON = '//button[@id="react-burger-menu-btn"]'
    HEADER_TEXT = '//div[@class="app_logo"]'
    TWITTER_LOGO_BUTTON = '//a[@href="https://twitter.com/saucelabs"]'
    FACEBOOK_LOGO_BUTTON = '//a[@href="https://www.facebook.com/saucelabs"]'
    LINKEDIN_LOGO_BUTTON = '//a[@href="https://www.linkedin.com/company/sauce-labs/"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._main_menu = self._driver.find_element(By.XPATH, self.MAIN_MENU_BUTTON)
        self._header_text = self._driver.find_element(By.XPATH, self.HEADER_TEXT)
        self._twitter_logo_button = self._driver.find_element(By.XPATH, self.TWITTER_LOGO_BUTTON)
        self._facebook_logo_button = self._driver.find_element(By.XPATH, self.FACEBOOK_LOGO_BUTTON)
        self._linkedin_logo_button = self._driver.find_element(By.XPATH, self.LINKEDIN_LOGO_BUTTON)

    def click_on_main_menu_button(self):
        self._main_menu.click()

    def header_text_string(self):
        return self._header_text.text

    def click_on_twitter_logo(self):
        self._twitter_logo_button.click()

    def click_on_facebook_logo(self):
        self._facebook_logo_button.click()

    def click_on_linkedin_logo(self):
        self._linkedin_logo_button.click()
