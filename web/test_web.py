from selenium import webdriver

class TestWeb(object):

    def test1(self):
        self.driver = webdriver.Chrome()
        webdriver.Remote
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.Re

        self.driver.execute_script("return JSON.stringify(window.performance.timing)")


if  "__main__" == __name__:
    test = TestWeb()
    test.test1()