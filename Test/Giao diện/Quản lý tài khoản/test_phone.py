from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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

# Truy cập trang qltk
driver.get("http://ec2-52-62-1-121.ap-southeast-2.compute.amazonaws.com:8080/user/account")

#Thêm std
driver.find_element(By.NAME, "phone").click()
driver.find_element(By.NAME, "phone").send_keys("0914859132")
driver.find_element(By.CSS_SELECTOR, ".ls-button_look_primary").click()
value = driver.find_element(By.NAME, "phone").get_attribute("value")
assert value == "0914859132"
# Đóng trình duyệt
driver.quit()

  
