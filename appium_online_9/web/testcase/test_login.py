#allure generate report/ -o report/html --clean  --- 生成html
#allure serve allure-results    ---- 启动server,没用，直接看html文件
#都在report上一级目录
from web.page.PC import PC
import pytest



class TestLogin(object):

    def setup_method(self):
        self.loginPage=PC.main().gotoLoginPage()

    def test_login_password(self):
        self.loginPage.loginByPassword("1000010", "admin123")

    def teardown_method(self):
        self.loginPage.logout()
