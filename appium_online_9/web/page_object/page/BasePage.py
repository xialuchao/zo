from selenium.webdriver.remote.webdriver import WebDriver
from web.page_object.driver.client import SeleniumDriver


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    # def __init__(self, driver):
        # self.driver:WebDriver = driver
    def __init__(self, driver):
        self.driver:WebDriver = self.get_driver()

    @classmethod
    def get_driver(cls):
        cls.driver = SeleniumDriver().init_selenium()
        # return cls.driver


    def find(self, kv):
        element = self.driver.find_element(*kv)
        return element

