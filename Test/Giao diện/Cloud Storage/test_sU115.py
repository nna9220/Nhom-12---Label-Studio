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

class TestSU115():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sU115(self):
    self.driver.get("http://localhost:8081/projects/?page=1")
    self.driver.set_window_size(1120, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".ls-projects-page__link:nth-child(2) .ls-project-card__title svg").click()
    self.driver.find_element(By.LINK_TEXT, "Settings").click()
    self.driver.find_element(By.LINK_TEXT, "Cloud Storage").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".ls-columns__item:nth-child(1) .ls-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-columns__item:nth-child(1) > .ls-storage-settings__controls > .ls-button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
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
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(5)").click()
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys("Demo_3")
    self.driver.find_element(By.NAME, "path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-form__submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".ls-form-indicator__item").text == "Connection failed"
  
