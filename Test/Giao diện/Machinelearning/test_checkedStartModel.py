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

class TestCheckedStartModel():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_checkedStartModel(self):
    self.driver.get("http://localhost:8080/projects/10/settings/ml")
    self.driver.set_window_size(960, 816)
    self.driver.find_element(By.NAME, "start_training_on_annotation_update").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_type_submit").click()
    assert self.driver.find_element(By.NAME, "start_training_on_annotation_update").is_selected() is True
  
