# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt WebDriver (ví dụ: Chrome)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Mở trang đăng ký Label Studio
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/user/login")

# Không nhập email
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("nna9220@gmail.com")
#pass
pass_input = driver.find_element(By.ID, "password")
pass_input.send_keys("nanguyen")

#Đăng nhập
register_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
register_button.click()

# Truy cập setup
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/projects?page=1")
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/projects/1/data?tab=1&page=1")
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/projects/1/settings/webhooks")
driver.set_window_size(945, 728)
driver.find_element(By.CSS_SELECTOR, ".ls-webhook-list__item-url").click()
driver.find_element(By.CSS_SELECTOR, ".ls-toggle:nth-child(2) > .ls-toggle__input").click()
driver.find_element(By.CSS_SELECTOR, ".ls-button_look_primary").click()
assert driver.find_element(By.NAME, "2").is_selected() is True
  
