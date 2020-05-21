from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver:WebDriver = driver

    def find(self, kv):
        element = self.driver.find_element(*kv)
        return element

