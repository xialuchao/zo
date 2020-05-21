from selenium.webdriver.common.by import By
import time

from web.page_object.page.BasePage import BasePage

class LoginPage(BasePage):
    _username = (By.ID, "loginId")
    _pwd = (By.ID, "password")
    _loginButton = (By.ID, "loginBtn")

    def loginByUsernamePwd(self, username, pwd):
        self.find(self._username).send_keys(username)
        self.find(self._pwd).send_keys(pwd)
        time.sleep(2)
        self.find(self._loginButton).click()
        return self

