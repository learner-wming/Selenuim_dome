from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://prerelease.simcards.cn/#/login')
driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/div/input').send_keys('sangjy')  # 用户名
driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/input').send_keys('123456')  # 密码
driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/button').click()  # 登录按钮
e = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/ul/li[1]/span')
print(e.__dict__)

# ？？ 这个首页的元素定位不到
