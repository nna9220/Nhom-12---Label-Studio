import unittest
from selenium import webdriver

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Chờ tối đa 10 giây cho mỗi yêu cầu tìm kiếm phần tử

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get('http://ec2-13-238-255-249.ap-southeast-2.compute.amazonaws.com:8080/user/login/')  # Thay thế 'your-label-studio-url' bằng URL của Label Studio
        # Thực hiện các thao tác đăng nhập
        # Ví dụ:
        username_input = self.driver.find_element_by_id('username')
        password_input = self.driver.find_element_by_id('password')
        login_button = self.driver.find_element_by_id('login-button')

        username_input.send_keys('nna9220@gmail.com')  # Thay thế 'your-username' bằng tên đăng nhập của bạn
        password_input.send_keys('nanguyen

        # Kiểm tra xem đăng nhập thành công hay không
        # Ví dụ:
        welcome_message = self.driver.find_element_by_xpath('//div[@class="welcome-message"]')
        self.assertEqual(welcome_message.text, 'Welcome, nna9220')  # Thay thế 'your-username' bằng tên đăng nhập của bạn

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=open('report.txt', 'w')))
