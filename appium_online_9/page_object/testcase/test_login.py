#allure generate report/ -o report/html --clean  --- 生成html
#allure serve allure-results    ---- 启动server,没用，直接看html文件
#都在report上一级目录
from appium_online_9.page_object.page.App import App
import pytest
import allure
# import sys
# sys.path.append('../../../../')

@allure.feature('登陆功能')
class TestLogin(object):
    # @classmethod
    # def setup_class(cls):
    #     cls.profilePage=App.main().gotoSelected()
    def setup_method(self):
        self.loginPage=App.main().gotoSelected()

    @pytest.mark.parametrize("user, password, msg", [
        ("133354984154651", "111111", "登录"),
        ("1000010", "111111", "登录"),
        ("1000333", "admin123", "账户余额")
    ])
    @allure.story('使用用户名密码登陆')
    def test_login_password(self, user, password,msg):

        self.loginPage.loginByPassword(user, password)
        # assert self.loginPage.elementExist("登陆")
        assert self.loginPage.elementExist(msg)# == True
        # assert msg in self.loginPage.getToast()


    def teardown_method(self):
        if self.loginPage.elementExist("账户余额"):
            self.loginPage.logout_account()
        else:
            print("teardown fail,account not login")