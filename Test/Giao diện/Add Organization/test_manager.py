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

class TestSU142():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sU142(self):
    self.driver.get("http://ec2-3-26-179-137.ap-southeast-2.compute.amazonaws.com:8080/organization?page=1")
    self.driver.set_window_size(1120, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("na@gmail.com")
    element = self.driver.find_element(By.CSS_SELECTOR, "select")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "select")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "select")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, "select").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, "select")
    dropdown.find_element(By.XPATH, "//option[. = 'manager']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_submit").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".ls-button_look_:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".state").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".state").text == "Successfully add person to organization"
    self.driver.find_element(By.CSS_SELECTOR, ".ls-modal__footer .ls-button_look_primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_text svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-people-list__user:nth-child(9) > .ls-email_iv").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".ls-people-list__user:nth-child(9) > .ls-email_iv").text == "na@gmail.com"
  
