import time
import allure
from selenium.webdriver.common.by import By
from web.page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions

class LoginPage(BasePage):
    _username = (By.ID, "loginId")
    _pwd = (By.ID, "password")
    _loginButton = (By.ID, "loginBtn")
    _logout = (By.LINK_TEXT, "退出")


    def loginByPassword(self, username, pwd):
        time.sleep(2)
        self.find(self._username).send_keys(username)
        self.find(self._pwd).send_keys(pwd)
        time.sleep(2)
        self.find(self._loginButton).click()
        return self

    # def logout(self):
    #     time.sleep(2)
    #     self.find(self._logout).click()
    #     # self.findByText("退出").click()

