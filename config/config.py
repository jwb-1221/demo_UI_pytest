from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from PIL import ImageGrab
import time
import sys
import lib
class config(object):
    "配置信息"
    def config(self):
        "配置浏览器信息"
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()
    def config_Chrome(self):
        pass
    def config_Firefox(self):
        self.dr = webdriver.Firefox(executable_path="")





