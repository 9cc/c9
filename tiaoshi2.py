# 动态查找元素
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.maximize_window()
driver.get('https://www.baidu.com')
locator = ('id', 'kw')
WebDriverWait(driver, 10).until(lambda s: s.find_element(*locator)).send_keys('软件测试')