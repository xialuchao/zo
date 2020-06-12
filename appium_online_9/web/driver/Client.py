from selenium import webdriver
import yaml
from selenium.webdriver import DesiredCapabilities
import threading
from multiprocessing import Process


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
#     def install_app(cls,url):# -> webdriver:
#         # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
#         # cls.driver = webdriver.Remote(command_executor='http://192.168.6.65:4567/wd/hub',
#         #                                desired_capabilities=DesiredCapabilities.CHROME)
#         for url in cls.get_env(cls)["drivers"]:
#             # if not cls.driver_exists():
#                 # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
#             remoteurl=('http://%s/wd/hub')%url
#             print(remoteurl)
#             cls.driver = webdriver.Remote(command_executor=remoteurl,
#                                            desired_capabilities=DesiredCapabilities.CHROME)
#         cls.driver.get("http://ft1.sh.zhaoonline.com")
#
#         # cls.driver = webdriver.Chrome("/Users/shylock/github/zo/appium_online_9/chromedriver")
#         return cls.driver


class SeleniumClient(object):
    driver: webdriver

    def get_env(self):
        with open("../data/get_driver.yaml") as f:
            k = f.read()
        remoteurl = yaml.load(k, Loader=yaml.FullLoader)
        return remoteurl

    @classmethod
    def driver_exists(cls):
        try:
            if cls.driver:
                print("$"*30)
                print("true")
                return True
        except:
            print("$" * 30)
            print("false")
            return False


    @classmethod
    def install_app(cls)-> webdriver:
        threads = []
        for url in cls.get_env(cls)["drivers"]:
            threads.append(threading.Thread(target=cls.create_drvier, args=(url,)))
            # P = Process(target=cls.create_drvier, args=(url,))
        for P in threads:
            P.start()
            P.join()

    @classmethod
    def create_drvier(cls,url):
        # if not cls.driver_exists():
            # cls.driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
        remoteurl = ('http://%s/wd/hub') % url
        cls.driver = webdriver.Remote(command_executor=remoteurl,
                                      desired_capabilities=DesiredCapabilities.CHROME)
        cls.driver.get("http://ft1.sh.zhaoonline.com")
        return cls.driver






