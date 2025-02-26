import time
from copy import copy

from basepage.basepage import BasePage
from util.read_yaml import ReadYaml
from time import sleep
from selenium.webdriver.common.keys import Keys
from util.read_ini import ini
from page.SekormPage.searchPage import searchPage
from page.SekormPage.planpricePage import PlanpricePage

sekorm = ReadYaml()


class IndexPage(BasePage):

    def go_search(self):  # 跳转搜索页面
        self.is_click(sekorm['搜索入口'])
        return searchPage(self.driver)

    def go_pricePage(self):  # 跳转计划价格页面
        self.is_click(sekorm['计划价格页面入口'])
        return PlanpricePage(self.driver)



if __name__ == '__main__':
    pass