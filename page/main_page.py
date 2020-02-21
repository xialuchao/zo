from appium.webdriver.common.mobileby import MobileBy

from driver.android_driver import AndroidDriver
from page.base_page import BasePage
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.profile_page import ProfilePage


class MainPage(BasePage):
    def __init__(self):
        self.driver = AndroidDriver.start_driver()

    def go_to_profile(self):
        self.driver.find(("ID","id")).click()
        return ProfilePage()

    def go_to_mine(self):
        self.find_text("我的").click()
        _account = (MobileBy.XPATH, '//*[@text="手机/昵称/客户编号"]')
        self.driver.implicitly_wait(5)
        if self.find(_account).is_displayed():
            return LoginPage()
        else:
            return MinePage()
