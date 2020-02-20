from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.base_page import BasePage
# from page.main_page import MainPage


class LoginPage(BasePage):

    _account = (MobileBy.XPATH, '//*[@text="手机/昵称/客户编号"]')
    _pwd = (MobileBy.XPATH, '//*[@text="密码"]')
    _login_button = (MobileBy.XPATH, '//*[@content-desc="登 录"]')

    def login_mobile(self, account, pwd):
        self.find(self._account).send_keys(account)
        # self.find((MobileBy.XPATH, '//*[@class="android.view.View" and @index="2"]//*[@class="android.view.View" and @index="1"]')).click()
        self.find(self._account).send_keys(pwd)
        self.find(self._login_button).click()
        return self

    def login_success(self):
        self.find(By.XPATH, 'id').click()
        return MainPage()

