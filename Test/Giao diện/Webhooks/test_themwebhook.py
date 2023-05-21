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

element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ls-button")))
element.click()
driver.find_element(By.NAME, "url").click()
driver.find_element(By.NAME, "url").send_keys("https://github.com/nna9220/Nhom-12---Label-Studio")
driver.find_element(By.CSS_SELECTOR, ".ls-button__icon > svg").click()
driver.find_element(By.CSS_SELECTOR, ".ls-webhook-detail__headers-input:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, ".ls-webhook-detail__headers-input:nth-child(1)").send_keys("A")
driver.find_element(By.CSS_SELECTOR, ".ls-input:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, ".ls-input:nth-child(2)").send_keys("3")
driver.find_element(By.CSS_SELECTOR, ".ls-button_look_primary").click()
assert driver.find_element(By.CSS_SELECTOR, ".ls-webhook-list__item:nth-child(2) > .ls-webhook-list__item-url").text == "https://github.com/nna9220/Nhom-12---Label-Studio"
# Đóng trình duyệt
driver.quit()

