import pytest
from isodate import Duration
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v109 import browser
from selenium.webdriver.common.keys import Keys
import sys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver_connect import get_connection


def open_label_interface(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("nna9220@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("nanguyen")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press create project button
    driver.implicitly_wait(15)
    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'ls-project-card__title-text') and text()='test label project']"))
    )
    project.click()

    # Press setting
    driver.implicitly_wait(15)
    settings_link = driver.find_element(By.XPATH, '//a[contains(@class, "ls-button_size_compact") and text()="Settings"]')
    settings_link.click()

    # Press label interface
    driver.implicitly_wait(15)
    lb_interface = driver.find_element(By.XPATH,
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Labeling Interface"]')
    lb_interface.click()

def browse_label_interface(driver):
    open_label_interface(driver)
    # Press browse template
    template = driver.find_element(By.XPATH, '//button[text()="Browse Templates"]')
    template.click()

    # Select template
    driver.implicitly_wait(15)
    image = driver.find_element(By.XPATH, '//ul/li[contains(@class, "ls-templates-list__template")][2]/img')
    image.click()

def test_create_label_xml():
    driver = get_connection()

    open_label_interface(driver)
    # Enter xml
    saveBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
    saveBtn.click()
    driver.close()


def test_select_template():
    driver = get_connection()

    browse_label_interface(driver)
    # Press save ls-button_look_primary
    saveBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
    saveBtn.click()
    driver.close()


def test_create_label_GUI():

    driver = get_connection()

    browse_label_interface(driver)

    #Add label
    driver.find_element(By.XPATH, '//textarea[contains(@name,"labels")]').send_keys("Test label")
    addBtn = driver.find_element(By.XPATH, '//input[contains(@value,"Add")]')
    addBtn.click()

    #Press save ls-button_look_primary
    saveBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
    saveBtn.click()
    driver.close()

def test_delete_label_GUI():
    driver = get_connection()

    browse_label_interface(driver)

    #Delete label
    deleteBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-configure__delete-label")][1]')
    deleteBtn.click()

    # Press save ls-button_look_primary
    saveBtn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
    saveBtn.click()
    driver.close()

def test_config_label_color():
    driver = webdriver.Chrome()
    driver.maximize_window()

    browse_label_interface(driver)

    #Press label
    driver.implicitly_wait(20)
    # Find the first input element with the type "color" using XPath
    first_color_input = driver.find_element(By.XPATH,'//input[@type="color"][1]')

    # Change the color to black
    first_color_input.send_keys("#000000")
    time.sleep(2)
    driver.close()