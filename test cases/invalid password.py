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
username_input.send_keys("TEST")
password_input.send_keys("pass123")
login_button.click()
time.sleep(2)

try:
    assert "Username and password do not match any user in this service" in driver.page_source
    print("TC005: Case Sensitivity – PASS")
except AssertionError:
    print("TC005: Case Sensitivity – FAIL (Incorrect case handling)")

driver.quit()
