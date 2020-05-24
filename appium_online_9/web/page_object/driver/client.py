from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class SeleniumDriver(object):
    driver:webdriver
    @classmethod
    def init_selenium(cls) -> webdriver:
        # cls.driver = webdriver.Remote(command_executor='http://192.168.6.242:4444/wd/hub',
        #                                desired_capabilities=DesiredCapabilities.CHROME)
        # cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)

        # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
        cls.driver = webdriver.Chrome("/Users/shylock/github/zo/appium_online_9/chromedriver")
        return cls.driver