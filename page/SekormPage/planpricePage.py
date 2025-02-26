from basepage.basepage import BasePage


locater = {
    'DevCraftUI' : '/html/body/div[1]/section[2]/div/div[2]/div[1]/div[4]/div[2]/div',
    'Complete': '/html/body/div[1]/section[2]/div/div[2]/div[1]/div[5]/div/div[2]/div',
    'UItimate': '/html/body/div[1]/section[2]/div/div[2]/div[1]/div[6]/div[2]/div'
}

class PlanpricePage(BasePage):

    def get_price1(self):
        return self.getvalue(locater['DevCraftUI'])