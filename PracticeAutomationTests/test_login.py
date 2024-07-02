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
    driver.find_element(By.ID, "password").send_keys("HiiGuys912")

    driver.find_element(By.NAME, "login").click()
    time.sleep(1)

    assert f"The username <strong>{username}</strong> is not registered on this site." \
           in driver.page_source, "Expected error message not found"

    driver.quit()


def test_login_sensitive_case():
    """
        Test case for incorrect username and invalid password.
    """
    driver = webdriver.Chrome()

    driver.get("https://practice.automationtesting.in/my-account/")
    time.sleep(1)

    username = "Bahaa.aboZlf57"
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("HiiGUys912")

    driver.find_element(By.NAME, "login").click()
    time.sleep(1)

    assert f"Error:" in driver.page_source, "Expected error message not found"

    driver.quit()


def test_login_authentication():
    """
        Test case for incorrect username and invalid password.
    """
    driver = webdriver.Chrome()

    # Enter the URL
    driver.get("http://practice.automationtesting.in/")

    # Click on My Account Menu
    my_account_link = driver.find_element(By.LINK_TEXT, "My Account")
    my_account_link.click()

    # Wait for the page to load
    time.sleep(1)

    # Enter the case-changed username in username textbox
    username_field = driver.find_element(By.ID, "username")
    username = "bahaa.abozlf57".swapcase()  # Example of changing case
    username_field.send_keys(username)

    # Enter the case-changed password in the password textbox
    password_field = driver.find_element(By.ID, "password")
    password = "HiiGuys912".swapcase()  # Example of changing case
    password_field.send_keys(password)

    # Click on login button
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait for login to complete
    time.sleep(2)

    # Once logged in, sign out of the site
    sign_out_link = driver.find_element(By.LINK_TEXT, "Logout")
    sign_out_link.click()

    # Wait for logout to complete
    time.sleep(2)

    # Now press the back button
    driver.back()

    # Optional: Wait for the page to load after navigating back
    time.sleep(2)

    # Check if the user is signed out by verifying the presence of elements on the general webpage
    assert "My Account" not in driver.page_source, "User is still logged in"

    # Close the browser
    driver.quit()