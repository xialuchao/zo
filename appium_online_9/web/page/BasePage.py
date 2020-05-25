from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from web.driver.Client import SeleniumClient
import yaml
import time
import re

class BasePage(object):
    element_black=[
        (By.XPATH, "ddd")
    ]
    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=SeleniumClient.driver
        return cls.driver

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

