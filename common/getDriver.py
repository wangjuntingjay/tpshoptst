import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from common.testlog import testlog


class Driver(object):

    def __init__(self, url, browser="chrome"):
        self.log = testlog()
        match browser:
            case "chrome":
                self.driver = webdriver.Chrome()
                self.log.test_info("测试开始，启动浏览器{}".format(browser))
            case "firefox":
                self.driver = webdriver.Firefox()
                self.log.test_info("测试开始，启动浏览器{}".format(browser))
            case "edge":
                self.driver = webdriver.Edge()
                self.log.test_info("测试开始，启动浏览器{}".format(browser))
            case "ie":
                self.driver = webdriver.Ie()
                self.log.test_info("测试开始，启动浏览器{}".format(browser))
        self.log.test_info("输入网址{}\n".format(url))
        self.driver.get(url)

    def find_web_element(self, by, ele):
        self.log.test_info("通过属性{}寻找元素{}".format(by, ele))
        try:
            return WebDriverWait(self.driver, timeout=3, poll_frequency=0.5).until(lambda x: x.find_element(by, ele))
        except:
            self.log.test_error("没有找到元素{}".format(ele))

    def get_driver(self):
        if self.driver != None:
            return self.driver
        else:
            self.log.test_error("浏览器未启动")

    def __del__(self):
        self.log.test_info("测试结束\n")

    def sleep(self, num):
        self.log.test_info("程序休眠{}秒".format(num))
        time.sleep(num)

    def click_element(self, *loc):
        try:
            self.ele = self.find_web_element(*loc)
            self.log.test_info("点击{}元素{}".format(*loc))
            self.ele.click()
        except:
            self.log.test_error("元素{}点击无反应".format(*loc))

    def send_keys(self, message, *loc):
        try:
            self.ele = self.clear_content(*loc)
            self.log.test_info("输入{}".format(message))
            self.ele.send_keys(message)
        except:
            self.log.test_error("无法输入{}".format(message))

    def start_test(self, name):
        self.log.test_info("开始执行测试用例{}".format(name))

    def end_test(self, name):
        self.log.test_info("结束执行测试用例{}\n".format(name))

    """清除内容"""
    def clear_content(self, *loc):
        try:
            self.ele = self.find_web_element(*loc)
            self.ele.clear()
            return self.ele
        except:
            self.log.test_error("无法清除{}{}的内容".format(*loc))