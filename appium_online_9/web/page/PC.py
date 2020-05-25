from web.page.BasePage import BasePage
from web.page.MainPage import MainPage


class PC(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().install_app()
        return MainPage()