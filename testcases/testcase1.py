from selenium import webdriver
from time import sleep
import pyautogui


def test1():
    print('test1')


# 直接使用使用ind_element_by_xpath()也能成功的定位到这个checkbox 那就不需要使用老师说的那个PyAutoGUI 模块了
def test2():
    driver = webdriver.Chrome()
    driver.get('http://prerelease.simcards.cn/#/login')
    driver.maximize_window()
    sleep(3)
    elem = driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[4]/div[1]/label/span[1]/span')
    rect = elem.rect
    print(rect)
    elem.click()
    sleep(3)


# 这个方法就是用老师所使用的PyAutoGUI模块来尝试完成"记住密码"这个checkbox，但是却勾选不中
def test3():
    driver = webdriver.Chrome()
    driver.get('http://prerelease.simcards.cn/#/login')
    driver.maximize_window()
    sleep(3)
    elem = driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[4]/div[1]/label/span[1]/span')
    rect = elem.rect
    print(rect)
    pyautogui.click(rect['x']+10, rect['y']+130)
    sleep(3)
