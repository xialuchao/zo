# from appium import webdriver
# from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
import yaml

class SeleniumClient(object):

    # driver:webdriver
    @classmethod
    def install_app(cls):# -> webdriver:
        # cls.driver = webdriver.Remote(command_executor='http://192.168.6.242:4444/wd/hub',
        #                                desired_capabilities=DesiredCapabilities.CHROME)
        # cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
        cls.driver.get("http://ft1.sh.zhaoonline.com")
        # cls.driver = webdriver.Chrome("/Users/shylock/github/zo/appium_online_9/chromedriver")
        return cls.driver
