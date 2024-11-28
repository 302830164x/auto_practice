from basepage.basepage import BasePage
from util.read_yaml import ReadYaml
from time import sleep

sekorm = ReadYaml()

class IndexPage(BasePage):

    def search(self, text):
        self.send_element(sekorm['搜索框'], text)
        sleep(3)
        self.is_click(sekorm['搜索按钮'])

