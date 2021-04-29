from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from PIL import ImageGrab
import time
import sys,os
config = os.path.dirname(os.path.dirname(__file__))
sys.path.append(config)
#谷歌浏览器
chromedriver = os.path.join(config,"lib","chromedriver.exe")
#火狐浏览器
geckodriver  = os.path.join(config,"lib","geckodriver.exe")
#截图路径
scrrrnshot_report = os.path.join(config,"report")

class config(object):
    "浏览器配置信息"
    def config(self):
        "配置浏览器信息"
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def config_Chrome(self):
        """打开谷歌浏览器
        隐式等待为10秒"""
        self.dr = webdriver.Chrome(executable_path=chromedriver)
        config()

    def config_Firefox(self):
        """打开火狐浏览器
        隐式等待为10秒"""
        self.dr = webdriver.Firefox(executable_path=geckodriver)
        config()







