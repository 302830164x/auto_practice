from selenium import webdriver
from basepage.basepage import BasePage
from util.read_yaml import ReadYaml

sekorm = ReadYaml()
locater = {
    '搜索结果1': '/html/body/div[1]/div/section[2]/div/div/div[3]/ul/li[1]/h4/a'
}

class searchPage(BasePage):

    def get_search_text1(self):
        self.send_element(sekorm['搜索框'], 'UI')
        self.is_click(sekorm['搜索按钮'])
        return self.getvalue(locater['搜索结果1'])


if __name__ == '__main__':
    a = searchPage()
    a.get_url('https://www.telerik.com/search')
    b = a.get_search_text1()
    print(b)



