import time

from selenium.webdriver.common.by import By

from common.Assert import AssertUnit
from common.getDriver import Driver


class Login(Driver, AssertUnit):

    def __init__(self, url="http://www.tpshop.cn/Home/user/login.html"):
        super().__init__(url)

    """输入账号"""

    def input_username(self, username):
        self.send_keys(username, By.ID, "username")
        # self.find_web_element(By.ID, "username").send_keys(username)

    """输入密码"""

    def input_password(self, password):
        self.send_keys(password, By.ID, "password")
        # self.find_web_element(By.ID, "password").send_keys(password)

    """输入验证码"""

    def input_verify_code(self, verify_code):
        self.send_keys(verify_code, By.ID, "verify_code")
        # self.find_web_element(By.ID, "verify_code").send_keys(verify_code)

    """点击登录"""

    def click_login(self):
        self.click_element(By.NAME, "sbtbutton", )
        # self.find_web_element(By.NAME, "sbtbutton").click()

    """刷新验证码"""

    def re_verify_code(self):
        self.click_element(By.ID, "verify_code_img")

    """错误信息"""

    def login_information(self):
        return self.find_web_element(By.CLASS_NAME, "layui-layer-content")

    """安全退出按钮"""

    def save_logout(self):
        return self.find_web_element(By.LINK_TEXT, "安全退出")

    """点击确定按钮"""

    def click_button_sure(self):
        self.click_element(By.CLASS_NAME, "layui-layer-btn0")

    # def click_button(self, *loc):
    #     self.find_web_element(*loc).click()
    #     time.sleep(3)

    """登录"""

    def login_success(self, kwargs):
        self.input_username(kwargs["username"])
        self.input_password(kwargs["password"])
        self.input_verify_code(kwargs["verify_code"])
        self.click_login()
        if kwargs["state"] != True:
            if kwargs["assert"]["except"] != None:
                self.assert_is_equal(self.login_information(), kwargs["assert"]["except"])
                self.click_button_sure()
        else:
            self.save_logout().click()
            self.driver.get(url="http://www.tpshop.cn/Home/user/login.html")
        self.sleep(2)

    def assert_is_equal(self, ele, exc):
        assert ele.text == exc
        pass

    def assert_is_exist(self, ele, **arges):
        assert self.save_logout() != None

    def assert_is_false(self, **arges):
        pass

    def assert_is_true(self, **arges):
        pass
