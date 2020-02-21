from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from driver.android_driver import AndroidDriver


class BasePage(object):
    def __init__(self):
        self.driver = AndroidDriver.driver
    # @classmethod
    # def get_driver(cls):
    #     print("=================get_driver===================")
    #     cls.driver = android_driver.AndroidDriver.start_driver()
    #     return cls.driver


    def find(self, kv):
        return self.driver.find_element(*kv)

    def find_text(self, text):
        print("=================find_text===================")
        return self.driver.find_element(By.XPATH,"//*[@text='%s']"%text)



