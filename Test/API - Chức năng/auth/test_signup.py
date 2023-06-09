import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection

def test_signup_success():
    driver = get_connection()
    driver.get("http://127.0.0.1:8080/user/signup")
    driver.find_element(By.NAME, "email").send_keys("nna9220@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("nanguyen")
    signupBtn = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
    signupBtn.click()
    driver.close()

def test_email_invalid():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux1234@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    driver.implicitly_wait(25)
    error = driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "User with this email already exists in this server"
    driver.close()

def test_password_invalid():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duc2kha2i6i1l71i8ntugx129q9527281@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("1")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    error = driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "Please enter a password 8-12 characters in length"
    driver.close()