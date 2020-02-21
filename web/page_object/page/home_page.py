from web.page_object.page.base_page import BasePage
from web.page_object.page.search_page import SearchPage


class HomePage(BasePage):

    def home_page_search(self, keyword): # , keyword):
        self.driver.find_element_by_id("keyword").click()
        self.driver.find_element_by_id("keyword").send_keys(keyword)
        self.driver.find_element_by_id("search-btn").click()
        return SearchPage(self.driver)
