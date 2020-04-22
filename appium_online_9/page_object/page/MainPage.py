from selenium.webdriver.common.by import By

from appium_online_9.page_object.page.BasePage import BasePage
# from appium_online_9.page_object.page.ProfilePage import ProfilePage
# from appium_online_9.page_object.page.SearchPage import SearchPage
from appium_online_9.page_object.page.LoginPage import LoginPage

# from appium_online_9.page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    _profile_button=(By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")
    # _mine = (By.XPATH, "//*[@text='我的']")
    _mine = "我的"

    def gotoSelected(self):
        #调用全局的driver对象使用webdriver api操纵app

        #self.driver.find_element(By.xpath, "//*[@text='自选']")

        # self.find(By.XPATH, "//*[@text='我的']")
        self.findByText(self._mine)
        #self.driver.find_element_by_xpath("//*[@text='自选']")
        self.findByText(self._mine).click()

        return LoginPage()

    # def gotoSearch(self) -> SearchPage:
    #     self.find(self._search_button).click()
    #     return SearchPage()
    #
    # def gotoProfile(self):
    #     #self.find(MainPage._profile_button).click()
    #     self.loadSteps("../data/MainPage.yaml", "gotoProfile")
    #     return ProfilePage()