from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver.support.wait import WebDriverWait


class TestLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://prerelease.simcards.cn/#/login')
        self.driver.maximize_window()

    def test_username_login_error(self):
        username = ''
        pwd = '123456'
        exp = self.driver.find_element_by_class_name('message-tips').text

        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/div/input').send_keys(username)  # 用户名
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/input').send_keys(pwd)  # 密码
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/button').click()  # 登录按钮

        # WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element) # 判断某个元素中的value属性值是否包含了预期字符串
        data = self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/div[2]').text
        assert data == exp   # assert 表达式 [, 参数]  为真时继续往下执行 抛出AssertionError错误，并将  参数  输出
        print('请输入用户名')

    def test_pwd_login_error(self):
        username = 'sangjy'
        pwd = '123456'

        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/div/input').send_keys(username)  # 用户名
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/input').send_keys(pwd)  # 密码
        self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/button').click()  # 登录按钮
        exp = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/ul/li[1]/span').tag_name
        print(exp)
        # WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element) # 判断某个元素中的value属性值是否包含了预期字符串
        data = '首页'
        assert data == exp  # assert 表达式 [, 参数]  为真时继续往下执行 抛出AssertionError错误，并将  参数  输出
        print('登录成功')

    def test_username_pwd_login_ture(self):
        pass
