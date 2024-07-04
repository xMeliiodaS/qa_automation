from selenium import webdriver
from selenium.webdriver.common.by import By

# LINKS_IN_PAGE = '//a'
#
# links_in_page = driver.find_elements(By.XPATH, LINKS_IN_PAGE)
#
# for link in links_in_page:
#     print(link.get_attribute("href"))

driver = webdriver.Chrome()
table = driver.find_element(By.ID, "table1")

rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
        print(col.text + "\t", end="")
    print()
driver.quit()


# Dynamic

def get_user_locator(username):
    return driver.find_element(By.XPATH, f'//a[text()="{username}"]')


def click_on_username(username):
    get_user_locator(username).click()
