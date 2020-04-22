from appium_online_9.page_object.page.App import App
import pytest

class TestLogin(object):
    # @classmethod
    # def setup_class(cls):
    #     cls.profilePage=App.main().gotoSelected()
    def setup_method(self):
        self.loginPage=App.main().gotoSelected()

    # @pytest.mark.parametrize("user, pw, msg", [
    #     ("156005347600", "111111", "手机号码"),
    #     ("15600534760", "111111", "密码错误")
    # ])
    def test_login_password(self):
        self.loginPage.loginByPassword()
        # assert msg in self.loginPage.getErrorMsg()

    # def teardown_method(self):
    #     self.loginPage.back()