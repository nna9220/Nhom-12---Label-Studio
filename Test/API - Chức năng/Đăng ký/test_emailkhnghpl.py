from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Khởi tạo trình duyệt WebDriver (ví dụ: Chrome)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Mở trang đăng ký Label Studio
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/user/signup")

# email
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("nna9220")
#Password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("nanguyen")

# Gửi form đăng ký
register_button = driver.find_element(By.XPATH, "//button[text()='Create Account']")
register_button.click()

# Kiểm tra thông báo lỗi
error_message = driver.find_element(By.CSS_SELECTOR, "li")
assert error_message.text == "Enter a valid email address."

# Đóng trình duyệt