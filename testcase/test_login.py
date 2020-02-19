
import  pytest

from page.base_page import BasePage
from page.main_page import MainPage


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        print("=================testcase_setup_class===================")
        cls.mainpage = MainPage().go_to_mine()

    def setup_method(self):
        # self.mainpage = MainPage().go_to_mine()
        pass

    def test_login_path(self):
        print("=================testcase_test_login_path===================")
        self.mainpage.click_account()
        # MainPage.go_to_profile().go_to_login().login_mobile(user, pw)
        # assert 1 == 1

