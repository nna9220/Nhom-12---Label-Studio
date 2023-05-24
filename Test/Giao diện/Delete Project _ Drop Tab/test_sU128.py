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

class TestSU128():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sU128(self):
    self.driver.get("http://localhost:8081/projects?page=1")
    self.driver.set_window_size(1120, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".ls-projects-page__link:nth-child(1) .ls-project-card__title-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dm-select-row .dm-checkbox__input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dm-tab-panel").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dm-space > .dm-dropdown__trigger:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(5) > .dm-menu__item_look_danger").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dm-button_size_compact:nth-child(1)").click()
  
