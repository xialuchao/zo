from web.page.BasePage import BasePage
from web.page.MainPage import MainPage
import yaml

class PC(BasePage):

    # def get_env(self):
    #     with open("../data/get_driver.yaml") as f:
    #         k = f.read()
    #     remoteurl = yaml.load(k, Loader=yaml.FullLoader)
    #     return remoteurl

    @classmethod
    def main(cls):
        # cls.getUrl()
        # for i in cls.get_env()["drivers"]:
        #     cls.getClient().install_app(i)
        #     return MainPage()
        cls.getClient().install_app()
        return MainPage()
