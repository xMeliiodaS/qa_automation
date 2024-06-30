import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_register_valid():
    driver = webdriver.Chrome()
    driver.get("http://practice.automationtesting.in/")
    driver.find_element(By.LINK_TEXT, "My Account").click()

    time.sleep(1)

    driver.find_element(By.ID, "reg_email").send_keys("pirem82009@joeroc.com")
    driver.find_element(By.ID, "reg_password").send_keys("HiiGuys912")

    register_button = driver.find_element(By.CSS_SELECTOR,
                                          "input.woocommerce-Button[name='register'][value='Register']")

    register_button.click()
    time.sleep(2)

    success_message = "Hello"
    assert success_message in driver.page_source

    driver.quit()


def test_register_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://practice.automationtesting.in/")
    driver.find_element(By.LINK_TEXT, "My Account").click()

    time.sleep(1)

    driver.find_element(By.ID, "reg_email").send_keys("iorhofawrg32w3gq3qg4984@nero3rqm")
    driver.find_element(By.ID, "reg_password").send_keys("HiiGuys912")

    register_button = driver.find_element(By.CSS_SELECTOR,
                                          "input.woocommerce-Button[name='register'][value='Register']")

    register_button.click()
    time.sleep(2)

    failure_message = " Please provide a valid email address."
    assert failure_message in driver.page_source, "Invalid email error message not found"

    driver.quit()


def test_register_empty_email():
    driver = webdriver.Chrome()
    driver.get("https://practice.automationtesting.in/my-account/")
    #   driver.find_element(By.LINK_TEXT, "My Account").click()

    time.sleep(1)

    driver.find_element(By.ID, "reg_email").send_keys("")
    driver.find_element(By.ID, "reg_password").send_keys("HiiGuys912")

    register_button = driver.find_element(By.CSS_SELECTOR,
                                          "input.woocommerce-Button[name='register'][value='Register']")

    register_button.click()
    time.sleep(2)

    failure_message = " Please provide a valid email address."
    assert failure_message in driver.page_source, "Empty email error message not found"


def test_register_empty_password():
    driver = webdriver.Chrome()
    driver.get("https://practice.automationtesting.in/my-account/")
    #   driver.find_element(By.LINK_TEXT, "My Account").click()

    time.sleep(1)

    driver.find_element(By.ID, "reg_email").send_keys("legof60747@devncie.com")
    driver.find_element(By.ID, "reg_password").send_keys("")

    register_button = driver.find_element(By.CSS_SELECTOR,
                                          "input.woocommerce-Button[name='register'][value='Register']")

    register_button.click()
    time.sleep(2)

    failure_message = " Please enter an account password."
    assert failure_message in driver.page_source, "Empty password error message not found"
