from selenium.webdriver.common.by import By

from web.page_object.page.BasePage import BasePage
from web.page_object.page.LoginPage import LoginPage
from web.page_object.page.SearchPage import SearchPage



class MainPage(BasePage):
    _login_button = (By.ID, "a_login")

    def enterLoginPage(self):
        self.find(self._login_button).click()
        return LoginPage(self.driver)