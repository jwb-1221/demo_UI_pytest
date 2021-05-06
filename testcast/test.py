from selenium import webdriver
import time
from config import URL,config,screenshot
import unittest
class TEST_1(unittest.TestCase):
    def test_1(self):
        config.config.config_Chrome_admin(self)
        time.sleep(3)
        screenshot.scrrrnshot.ImageGrab(self,interface="登录界面")
    def test_2(self):
        config.config.config_Firefox_admin(self)
        time.sleep(10)
