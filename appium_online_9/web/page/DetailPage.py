from selenium.webdriver.common.by import By
from web.page.BasePage import BasePage

class DetailPage(BasePage):
    _bid_button = (By.ID, "_btn_xiangqing_bid")

    def click_bid(self):
        self.find(self._bid_button).click()