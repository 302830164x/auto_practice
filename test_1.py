from page.SekormPage.index import IndexPage
from selenium import webdriver
from util.config import cm
from util.read_ini import ini





class Test1:

    def test1(self, driver):
        driver.get_url(ini.SekormUrl)
        driver.search('mcu')


