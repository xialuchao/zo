from appium.webdriver import webdriver
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidDriver(object):
    driver: WebDriver
    @classmethod
    def start_driver(cls):
        print("=================start_driver===================")
        caps = {}
        #如果有必要，进行第一次安装
        # caps["app"]=''
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.zhaoonline.www"
        caps["appActivity"] = ".ui.SplashActivity"
        #解决第一次启动的问题
        caps["autoGrantPermissions"] = "true"
        # caps['noReset']=True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

