from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

username_input.clear()
password_input.clear()
login_button.click()
time.sleep(2)

try:
    assert "Username is required" in driver.page_source
    print("TC003: Empty Fields – PASS")
except AssertionError:
    print("TC003: Empty Fields – FAIL (Required field error not shown)")

driver.quit()
