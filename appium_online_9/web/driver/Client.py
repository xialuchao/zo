# from appium import webdriver
# from appium.webdriver.webdriver import WebDriver
from selenium import webdriver
import yaml
from selenium.webdriver import DesiredCapabilities
import threading


# class SeleniumClient(object):
#
#     def get_env(self):
#         with open("../data/get_driver.yaml") as f:
#             k = f.read()
#         remoteurl = yaml.load(k, Loader=yaml.FullLoader)
#         return remoteurl
#
#     @classmethod
#     def driver_exists(cls):
#         try:
#             if cls.driver:
#                 return True
#         except:
#             return False
#
#     # driver:webdriver
#     @classmethod
#     def install_app(cls):# -> webdriver:
#         # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
#         # cls.driver = webdriver.Remote(command_executor='http://192.168.6.65:4567/wd/hub',
#         #                                desired_capabilities=DesiredCapabilities.CHROME)
#         for url in cls.get_env(cls)["drivers"]:
#             if not cls.driver_exists():
#                 # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
#                 remoteurl=('http://%s/wd/hub')%url
#                 print(remoteurl)
#                 cls.driver = webdriver.Remote(command_executor=remoteurl,
#                                                desired_capabilities=DesiredCapabilities.CHROME)
#             cls.driver.get("http://ft1.sh.zhaoonline.com")
#
#         # cls.driver = webdriver.Chrome("/Users/shylock/github/zo/appium_online_9/chromedriver")
#         return cls.driver
#

class SeleniumClient(object):

    def get_env(self):
        with open("../data/get_driver.yaml") as f:
            k = f.read()
        remoteurl = yaml.load(k, Loader=yaml.FullLoader)
        return remoteurl

    @classmethod
    def driver_exists(cls):
        try:
            if cls.driver:
                return True
        except:
            return False

    # driver:webdriver
    @classmethod
    def install_app(cls, url):  # -> webdriver:
        if not cls.driver_exists():
            # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
            remoteurl = ('http://%s/wd/hub') % url
            cls.driver = webdriver.Remote(command_executor=remoteurl,
                                          desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.get("http://ft1.sh.zhaoonline.com")
        return cls.driver

    def run(self):
        threads = []
        for url in self.get_env()["drivers"]:
            threads.append(threading.Thread(target=self.install_app, args=(url)))





