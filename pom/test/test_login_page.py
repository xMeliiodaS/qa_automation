import unittest

from selenium import webdriver

from logic.practice_test_login_page import PracticeTestLoginPage


class TestLoginPage(unittest.TestCase):

    def test_login_successfully(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        login_page = PracticeTestLoginPage(driver)

        # Steps in test case
        # login_page.fill_user_name_input("username")
        # login_page.fill_password_input("Password123")
        # login_page.click_submit_button()

        login_page.login_flow("student", "Password123")
        login_page.click_on_home_header_button()

    def test_login_unsuccessfully(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        login_page = PracticeTestLoginPage(driver)

        # login_page.fill_user_name_input("username234")
        # login_page.fill_password_input("Hi3552d")
        # login_page.click_submit_button()

        # Invalid data
        login_page.login_flow("username234", "Hi3552d")
