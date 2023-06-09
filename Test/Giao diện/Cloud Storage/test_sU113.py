# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSU113():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sU113(self):
    self.driver.get("http://localhost:8081/projects/?page=1")
    self.driver.set_window_size(1120, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".ls-projects-page__link:nth-child(1) .ls-project-card__title svg").click()
    self.driver.find_element(By.LINK_TEXT, "Settings").click()
    self.driver.find_element(By.LINK_TEXT, "Cloud Storage").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-columns__item:nth-child(1) .ls-button").click()
    element = self.driver.find_element(By.NAME, "storage_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.NAME, "storage_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.NAME, "storage_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.NAME, "storage_type").click()
    dropdown = self.driver.find_element(By.NAME, "storage_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Microsoft Azure']").click()
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys("demo")
    self.driver.find_element(By.NAME, "container").click()
    self.driver.find_element(By.NAME, "container").send_keys("nhom12")
    self.driver.find_element(By.NAME, "regex_filter").click()
    self.driver.find_element(By.NAME, "regex_filter").send_keys(".*")
    self.driver.find_element(By.NAME, "account_name").click()
    self.driver.find_element(By.NAME, "account_name").send_keys("us-east-1")
    self.driver.find_element(By.CSS_SELECTOR, ".ls-form__row:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-form__submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".ls-form-indicator__item").text == "Successfully connected!"
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_submit").click()
  
