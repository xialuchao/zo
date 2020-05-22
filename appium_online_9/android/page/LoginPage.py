import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium_online_9.page_object.page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions

class LoginPage(BasePage):
    _close_locator=(By.ID, "iv_close")
    _other_locator=(By.ID, "tv_login_by_phone_or_others")
    _register_phone_number=(By.ID, "register_phone_number")
    _register_code=(By.ID, "register_code")
    _button_next=(By.ID, "button_next")
    _tv_login_with_account=(By.ID, "tv_login_with_account")
    _login_account=(By.ID, "login_account")
    _login_password=(By.ID, "login_password")
    _close2_locator=(By.ID, "iv_action_back")
    _error_msg=(By.ID, "md_content")
    _back_locator=(By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")
    _username = "手机/昵称/客户编号"
    _password = "密码"
    _loginButton = (By.XPATH, "//android.view.View[@content-desc='登 录']")
    # _toast = (By.XPATH, "//*[@class='cube-toast-tip']")
    _mine = "我的"
    _setting_btn = (By.ID, "m_tool_set_btn")
    _logout_btn = (By.ID, "btn_logout_set")
    _yes_btn = "是"

    def loginByWX(self):
        return self
    def loginByMSG(self, phone, code):
        return self

    def loginByPassword(self, username, password):
        self.findByText(self._username).send_keys(username)
        self.findByText(self._password).send_keys(password)
        self.find(self._loginButton).click()

        # self.loadSteps("../data/LoginPage.yaml", "loginByPassword", var1=account, var2=password)
        return self
    # def loginSuccessByPassword(self, account, password):
    #     from page_object.page.MainPage import MainPage
    #     return MainPage()
    #
    # def back(self):
    #     self.find(self._back_locator).click()
    #     #WebDriverWait(self.driver, 2).until(expected_conditions.presence_of_element_located(self._close_locator))
    #     from page_object.page.ProfilePage import ProfilePage
    #     return ProfilePage()
    #
    def getErrorMsg(self):
        msg=self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg
    def getToast(self):
        print(111111111111111111111)
        try:
            msg=self.find(self._toast).text
            print(msg)
            return msg
        except:
            print("havent got toast")

    @allure.step("元素是否存在")
    def elementExist(self, text):
        time.sleep(5)
        source = self.driver.page_source
        # print(source)
        if text in source:
            return True
        else:
            return False

    @allure.step("退出账号")
    def logout_account(self):
        self.findByText(self._mine).click()
        if self.elementExist("账户余额"):
            self.find(self._setting_btn).click()
            self.swipe_up()
            self.find(self._logout_btn).click()
            self.findByText(self._yes_btn).click()
        else:
            print("havent login")




