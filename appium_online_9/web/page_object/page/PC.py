from web.page_object.page.BasePage import BasePage
from web.page_object.page.MainPage import MainPage


class PC(BasePage):
    @classmethod
    def main(cls):
        cls.get_driver()
        return MainPage()
