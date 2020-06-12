from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.driver.Client import SeleniumClient
import yaml
import time
import re

class BasePage(object):
    _logout = (By.LINK_TEXT, "退出")

    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=SeleniumClient.driver
        return cls.driver

    # @classmethod
    # def getUrl(cls):
    #     cls.driver = SeleniumClient.open_web()
    #     return cls.driver

    @classmethod
    def getClient(cls):
        return SeleniumClient

    # def find(self, kv) -> WebElement:
    #     #todo: 处理各类弹框
    #     return self.find(*kv)

    def find(self, kv):
        element: WebElement
        element=self.driver.find_element(*kv)
        return element

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" %text))

    # auctionid 藏品的数据库id
    def enterWeb(self, acutionid):
        self.driver.get("http://ft1.sh.zhaoonline.com/jiteyoupiao/%d.shtml"%acutionid)

    def logout(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self._logout))
        self.find(self._logout).click()

    def quitBro(self):
        self.driver.quit()


