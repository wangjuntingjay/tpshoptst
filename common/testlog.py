import logging
import os
import time


class testlog:
    """创建日志对象"""

    def __init__(self):
        self.logger = logging.getLogger()
        """设置日志文件位置"""
        self.handle = logging.FileHandler(filename=os.path.join(os.path.abspath(__file__ + "/../../report")+os.path.sep)+"{}test.log".format(time.strftime("%Y-%m-%d-%H-%M-%S")),
                                          encoding='utf-8')
        """设置日志级纪录别"""
        self.logger.setLevel(level=logging.INFO)

        """设置日志记录格式"""
        self.format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.handle.setFormatter(self.format)

        self.logger.addHandler(self.handle)

    def test_debug(self, message):
        self.logger.debug(message)

    def test_info(self, message):
        self.logger.info(message)

    def test_warning(self, message):
        self.logger.warning(message)

    def test_error(self, message):
        self.logger.error(message)

    def test_critical(self, message):
        self.logger.critical(message)

