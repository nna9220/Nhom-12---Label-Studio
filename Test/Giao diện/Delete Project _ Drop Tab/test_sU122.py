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

class TestSU122():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sU122(self):
    self.driver.get("http://localhost:8081/projects?page=1")
    self.driver.set_window_size(1120, 680)
    self.driver.find_element(By.CSS_SELECTOR, ".ls-projects-page__link:nth-child(1) .ls-project-card__title svg").click()
    self.driver.find_element(By.LINK_TEXT, "Settings").click()
    self.driver.find_element(By.LINK_TEXT, "Danger Zone").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-button_look_").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ls-label__text").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".ls-label__description").text == "Perform these actions at your own risk. Actions you take on this page can\\\'t be reverted. Make sure your data is backed up."
  
