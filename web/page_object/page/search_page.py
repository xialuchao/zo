from web.page_object.page.base_page import BasePage


class SearchPage(BasePage):

    def enter_detail(self):
        self.driver.find_element_by_class_name("toolong w160 iblock").click()
        return self