from selenium import webdriver
from config import URL
import time
import sys,os
config = os.path.dirname(os.path.dirname(__file__))
sys.path.append(config)
#截图路径
scrrrnshot_report = os.path.join(config,"report"+"/")

class config(object):
    "浏览器配置信息"
    def config(self):
        "配置浏览器信息"
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def config_Chrome_admin(self):
        """打开谷歌浏览器
        进入运营端
        隐式等待为10秒"""
        self.dr = webdriver.Chrome()
        config.config(self)
        self.dr.get(URL.URL.admin_url(self))

    def config_Chrome_merchant(self):
        """打开谷歌浏览器
        进入商户端
        隐式等待为10秒"""
        self.dr = webdriver.Chrome()
        config.config(self)
        self.dr.get(URL.URL.merchant_url(self))

    def config_Firefox_admin(self):
        """打开火狐浏览器
        进入运营端
        隐式等待为10秒"""
        self.dr = webdriver.Firefox()
        config.config(self)
        self.dr.get(URL.URL.admin_url(self))

    def config_Firefox_merchant(self):
        """打开火狐浏览器
        进入运营端
        隐式等待为10秒"""
        self.dr = webdriver.Firefox()
        config.config(self)
        self.dr.get(URL.URL.merchant_url(self))

