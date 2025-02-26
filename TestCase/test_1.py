import pytest
import allure
from page.SekormPage.index import IndexPage
from selenium import webdriver
from util.config import cm
from util.read_ini import ini

@allure.epic('测试练习平台')
@allure.feature('测试练习模块')
class Test_1:

    @pytest.fixture(scope='function', autouse=True)
    def init_driver(self, driver):
        self.a = driver
        self.a.get_url('https://www.telerik.com/support/demos')

    @allure.story('用例1')
    @allure.description('这是第一个测试用例')
    def test_1(self):
        text1 = self.a.go_search().get_search_text1()
        assert 'UI' in text1

    @allure.story('用例2')
    @allure.description('这是第二个测试用例')
    def test_2(self):
        text2 = self.a.go_pricePage().get_price1()
        assert '1,149' in text2

