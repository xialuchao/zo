from selenium.webdriver.common.by import By
from web.page.BasePage import BasePage
from web.page.LoginPage import LoginPage

class MainPage(BasePage):
    _login_button = (By.ID, "a_login")

    def gotoLoginPage(self):
        #调用全局的driver对象使用webdriver api操纵app
        self.find(self._login_button).click()
        return LoginPage()
