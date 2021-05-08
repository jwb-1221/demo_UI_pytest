import time
from config import config
from lib import screenshot
from common import browser
import unittest
class TEST_1(unittest.TestCase):
    def test_1(self):
        browser.config.config_Chrome_admin(self)
        time.sleep(2)
        screenshot.scrrrnshot("登录").ImageGrab()
    def test_2(self):
        config.config.config_Chrome_admin(self)
        time.sleep(2)
