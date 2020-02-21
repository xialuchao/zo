import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestWeb(object):

    def test1(self):
        #   本地执行
        # self.driver = webdriver.Chrome()
        #   远程执行
        self.driver = webdriver.Remote(command_executor='http://169.254.111.121:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.add_cookie()
        # self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        # self.driver.Re

        # self.driver.execute_script("return JSON.stringify(window.performance.timing)")
        time.sleep(10)
        self.driver.quit()


if  "__main__" == __name__:
    test = TestWeb()
    test.test1()