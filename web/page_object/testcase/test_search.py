import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

from web.page_object.page.home_page import HomePage


class TestCase(object):
    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://169.254.111.121:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver.add_cookie()
        # self.driver.maximize_window()
        self.driver.get("http://www.zhaoonline.com")
        # self.Home = HomePage(self.driver)
        # self.driver.Re
        # self.driver.execute_script("return JSON.stringify(window.performance.timing)")

    def test_search(self):
        # self.Home.home_page_search("熊猫金币").enter_detail()
        HomePage(self.driver).home_page_search("熊猫金币").enter_detail()
        # self.search()


    # def search(self):
    #     self.driver.find_element_by_id("keyword").click()
    #     self.driver.find_element_by_id("keyword").send_keys("熊猫金币")
    #     self.driver.find_element_by_id("search-btn").click()

    def teardown(self):
        time.sleep(10)
        self.driver.quit()
