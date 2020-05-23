from appium_online_9.page_object.driver.Client import AndroidClient
from appium_online_9.page_object.page.BasePage import BasePage
from appium_online_9.page_object.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return MainPage()