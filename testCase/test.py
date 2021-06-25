import time
from config import config
from lib import screenshot
from common import browser
from testCase import ceshishuju

import unittest
class TEST_1(unittest.TestCase):
    def test_1(self):
        browser.config.config_Chrome_admin(self)
        time.sleep(2)
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[1]/div/div/div/input').send_keys(ceshishuju.shuju.shuju1[0]["user"])
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[2]/div/div/div[1]/input').send_keys(ceshishuju.shuju.shuju1[0]["user"])
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/form/div[3]/div/div/div[1]/div/div/input').send_keys(ceshishuju.shuju.shuju1[0]["user"])
        time.sleep(10)
        screenshot.scrrrnshot("登录").ImageGrab()
    def test_2(self):
        config.config.config_Chrome_admin(self)
        time.sleep(2)

if __name__ == "__main__":
    TEST_1.test_1()
