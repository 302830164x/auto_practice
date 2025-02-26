from time import sleep

import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver:webdriver = None):
        self.driver = driver
        if not self.driver:
            self.driver = webdriver.Edge()

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def get_url(self, url):
        try:
            self.driver.get(url)
        except TimeoutException:
            print('连接超时{}'.format(TimeoutException))
        except InvalidArgumentException:
            print(f'URL错误：{InvalidArgumentException}')

    def find_element(self, element):
        ele = self.wait.until(EC.presence_of_element_located((By.XPATH, element)))
        return ele

    # def element_move_to_center(self, element):  # 滑动滑动轮将元素移动到页面中央
    #     ele = self.find_element(element)
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def is_click(self, element):    # 还可以使用鼠标点击，js模拟点击
        self.find_element(element).click()
        sleep(0.2)

    def send_element(self, element, value):
        ele = self.find_element(element)
        ele.clear()
        ele.send_keys(value)

    def getvalue(self, element):
        ele = self.find_element(element)
        if ele.is_displayed():
            text1 = ele.text
        return text1
