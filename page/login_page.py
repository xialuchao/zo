from selenium.webdriver.common.by import By

from page.base_page import BasePage
# from page.main_page import MainPage


class LoginPage(BasePage):

    def login_mobile(self, account, pwd):
        self.find(By.XPATH, 'id').click()
        self.find(By.XPATH, 'id').send_keys(account)
        self.find(By.XPATH, 'id').send_keys(pwd)
        self.find(By.XPATH, 'id').click()
        return self

    def login_success(self):
        self.find(By.XPATH, 'id').click()
        return MainPage()

