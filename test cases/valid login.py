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
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()
time.sleep(2)

try:
    inventory = driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory is not None
    print("TC001: Valid Login – PASS")
except AssertionError:
    print("TC001: Valid Login – FAIL (Dashboard not loaded)")

driver.quit()
