from selenium import webdriver
import time
from config import URL,config,screenshot
import unittest
class TEST(unittest.TestCase):
    def test_1(self):
        config.config.config_Chrome(self)
        time.sleep(10)

        # self.dr = webdriver.Firefox(executable_path = r"D:\request\腾讯云代码库\demo_UI\lib\geckodriver.exe")
        # self.dr.implicitly_wait(15)
        # self.dr.maximize_window()
        # self.dr.get(url='http://account-admin-webos-test.lastmiles.cn/#/')
        # time.sleep(10)
