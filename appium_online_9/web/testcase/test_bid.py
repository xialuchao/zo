import sys
sys.path.append('./../../')

from web.page.PC import PC
from web.page.BasePage import BasePage
import time
import pytest


class TestBid(object):
    def setup_class(self):
        self.mainPage = PC.main()
        self.mainPage.gotoLoginPage().loginByPassword("1000010","admin123")

    def setup_method(self):
        print("#"*30)
        time.sleep(2)
        self.detailPage = self.mainPage.gotoDetailPage(3827666)
        print(self.detailPage)

    def test_bid(self):
        self.detailPage.click_bid()

    def teardown_method(self):
        self.mainPage.logout()
        # self.mainPage.gotoLoginPage().logout()

    def teardown_class(self):
        self.mainPage.quitBrowser()