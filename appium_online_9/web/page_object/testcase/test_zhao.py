from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from web.page_object.page.MainPage import MainPage
from web.page_object.page.ProfilePage import ProfilePage
from web.page_object.testcase.BaseTestCase import BaseTestCase
from web.page_object.page.LoginPage import LoginPage
from web.page_object.page.BasePage import BasePage
from web.page_object.page.PC import PC


class TestZhao(BaseTestCase):

    def setup(self):
        # self.driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME,command_executor='http://192.168.6.242:4444/wd/hub')
        # self.driver=webdriver.Remote(command_executor='http://192.168.6.242:4444/wd/hub', desired_capabilities = DesiredCapabilities.CHROME)
        # self.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
        self.driver = PC.get_driver()
        print(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.get("http://ft1.sh.zhaoonline.com/")
        self.main=MainPage(self.driver)
        self.loginpage = self.main.enterLoginPage()

    # def test_search(self):
    #     self.main.search("alibaba").follow("1688")
    #     #todo: add assertion
    #
    # def test_profile(self):
    #     profile=ProfilePage(self.driver)
    #     profile.login()
    #     selected=profile.gotoSelected()
    #     selected.select("alibaba", "1688")
    #
    # def test_log(self):
    #     self.log.warning("warning demo")
    #     self.log.debug("debug demo")
    def test_login(self):
        self.loginpage.loginByUsernamePwd("1000010", "admin123")


    def teardown(self):
        sleep(10)
        self.driver.quit()