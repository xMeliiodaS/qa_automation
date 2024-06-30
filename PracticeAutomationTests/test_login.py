import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_valid():
    """
    Test case for valid login.
    """
    driver = webdriver.Chrome()

    driver.get("https://practice.automationtesting.in/my-account/")
    time.sleep(1)

    driver.find_element(By.ID, "username").send_keys("Bahaa.abozlf57")
    driver.find_element(By.ID, "password").send_keys("HiiGuys912")

    driver.find_element(By.NAME, "login").click()
    time.sleep(1)

    assert "Hello" in driver.page_source
    driver.quit()
