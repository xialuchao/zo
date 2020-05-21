from selenium.webdriver.common.by import By

from web.page_object.page.BasePage import BasePage
from web.page_object.page.LoginPage import LoginPage



class MinePage(BasePage):
    _login_button = (By.ID, "a_login")

    # def search(self, keyword):
    #     self.driver.find_element_by_name("q").send_keys(keyword)
    #     self.driver.find_element_by_css_selector(".nav__search button").click()
    #     return SearchPage(self.driver)

    def enterLoginPage(self):
        self.find(self._login_button).click()
        return LoginPage(self.driver)
        # self.driver.find_element_by_id("a_login").click()