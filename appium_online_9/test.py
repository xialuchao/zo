# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def a():
    for host in ["192.168.16.78:5555","192.168.6.100:6666"]:
        driver = webdriver.Remote(command_executor="192.168.16.78:5555", desired_capabilities=DesiredCapabilities.CHROME)

        driver.get("http://www.baidu.com")
        # driver.find_element_by_id("kw").send_keys(u"中国")
        # driver.find_element_by_id("su").click()
        time.sleep(3)
        if driver.title == u"中国_百度搜索":
            print("title匹配！")
        else:
            print("title不匹配！")
        driver.close()
a()