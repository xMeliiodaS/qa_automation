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


def test_login_incorrect_username_password():
    """
    Test case for incorrect username and invalid password.
    """
    driver = webdriver.Chrome()

    driver.get("https://practice.automationtesting.in/my-account/")
    time.sleep(1)

    username = "Bahaa.abozlf5753g"
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("HiiGuys912erg3")

    driver.find_element(By.NAME, "login").click()
    time.sleep(1)

    assert f"The username <strong>{username}</strong> is not registered on this site." \
           in driver.page_source, "Expected error message not found"

    driver.quit()
