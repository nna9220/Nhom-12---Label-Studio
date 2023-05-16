import pytest
from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection

def test_login_success():
    driver = get_connection()

    driver.get("http://ec2-54-252-209-102.ap-southeast-2.compute.amazonaws.com:8080/user/login/")

    driver.find_element(By.NAME, "email").send_keys("nna9220@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("nanguyen")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    driver.close()

def test_login_failure():
    driver = get_connection()

    driver.get("http://ec2-54-252-209-102.ap-southeast-2.compute.amazonaws.com:8080/user/login/")

    driver.find_element(By.NAME, "email").send_keys("nna9220@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("nanguyen")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()

    errorTxt = driver.find_element(By.CLASS_NAME, "error")

    assert errorTxt.text == "The email and password you entered don't match."
    driver.close()
