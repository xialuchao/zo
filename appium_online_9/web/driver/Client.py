# from appium import webdriver
# from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
import yaml
from selenium.webdriver import DesiredCapabilities


class SeleniumClient(object):

    @classmethod
    def driver_exists(cls):
        try:
            if cls.driver:
                return True
        except:
            return False

    # driver:webdriver
    @classmethod
    def install_app(cls):# -> webdriver:
        # cls.driver = webdriver.Remote(command_executor='http://192.168.6.242:4444/wd/hub',
        #                                desired_capabilities=DesiredCapabilities.CHROME)
        # cls.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
        if not cls.driver_exists():
            cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
            # cls.driver = webdriver.Remote(command_executor='http://192.168.6.90:4444/wd/hub',
            #                                desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.get("http://ft1.sh.zhaoonline.com")

        # cls.driver = webdriver.Chrome("/Users/shylock/github/zo/appium_online_9/chromedriver")
        return cls.driver

