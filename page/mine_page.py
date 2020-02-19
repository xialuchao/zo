from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class MinePage(BasePage):

    def click_account(self):
        # / [@class =android.widget.EditText]
        print("=================click_account===================")
        self.find((MobileBy.CLASS_NAME, "android.widget.EditText")).send_keys("13817462062")
        self.driver.find_element_by_xpath('//*[@class="android.view.View" and @index="2"]//*[@class="android.view.View" and @index="1"]').click()
        # self.driver.find_element_by_xpath('//*[@content-desc="登 录"]').click()
        # return self

