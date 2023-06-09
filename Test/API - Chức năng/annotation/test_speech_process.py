
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.driver_connect import get_connection


def open_annotation_interface(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("nna9220@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("nanguyen")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # open project

    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ls-projects-page__link')][5]"))
    )
    project.click()





    # open annotation interface
    # Wait until the label button is present and clickable
    task = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dm-table__row-wrapper")][1]'))
    )

    # Click the label button
    task.click()

def test_submit_annotation():
    driver = get_connection()
    open_annotation_interface(driver)

    # annotate
    transcription = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//textarea[contains(@aria-label,"TextArea Input")]'))
    )
    transcription.send_keys("Test transcription")

    # Press add button
    add_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ant-btn ant-btn-primary")]')
    add_btn.click()

    # Press submit
    try:
        submit_btn = driver.find_element(By.XPATH, '//button[contains(@class, "lsf-button_look_primary") and text()="Submit"]')
        submit_btn.click()
    except NoSuchElementException:
        update_annotation()

    driver.close()

def update_annotation():
    driver = get_connection()
    open_annotation_interface(driver)

    # Press Update
    submit_btn = driver.find_element(By.XPATH,
                                     '//button[contains(@class, "lsf-button_look_primary") and text()="Update"]')
    submit_btn.click()

    driver.close()
