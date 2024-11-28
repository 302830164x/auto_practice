from page.SekormPage.index import IndexPage
from selenium import webdriver
from util.config import cm
from util.read_ini import ini


a = IndexPage()


class Test1:

    def test1(self):

        a.get_url(ini.SekormUrl)
        a.search('mcu')


