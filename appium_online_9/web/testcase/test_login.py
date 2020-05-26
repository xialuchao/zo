#allure generate report/ -o report/html --clean  --- 生成html
#allure serve allure-results    ---- 启动server,没用，直接看html文件
#都在report上一级目录
import sys
sys.path.append('./../../')

from web.page.PC import PC
import pytest

class TestLogin(object):

    def setup_method(self):
        self.mainPage = PC.main()
        self.loginPage = self.mainPage.gotoLoginPage()

    def test_login_password(self):
        self.loginPage.loginByPassword("1000010", "admin123")

    def test_login_phone(self):
        self.loginPage.loginByPassword("1000333", "admin123")

    def teardown_method(self):
        self.mainPage.logout()
        # self.loginPage.logout()
