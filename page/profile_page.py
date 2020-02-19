from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage
from page.login_page import LoginPage


class ProfilePage(BasePage):

    def go_to_login(self):
        self.find((MobileBy.XPATH,'//*[@text="login"]')).click()
        return LoginPage()