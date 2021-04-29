from selenium import webdriver
from config import URL
import time
import sys,os
config = os.path.dirname(os.path.dirname(__file__))
sys.path.append(config)
#谷歌浏览器
chromedriver = "r'"+(os.path.join(config,"lib","chromedriver.exe")).replace("/", "\\")+"'"
#火狐浏览器
geckodriver  = "r'"+(os.path.join(config,"lib","geckodriver.exe")).replace("/", "\\")+"'"
#截图路径
scrrrnshot_report = str(os.path.join(config,"report")).replace("/", "\\")

abc = str(chromedriver)
print(abc)
class config(object):
    "浏览器配置信息"
    def config(self):
        "配置浏览器信息"
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def config_Chrome(self):
        """打开谷歌浏览器
        隐式等待为10秒"""
        self.dr = webdriver.Chrome()
        config.config(self)
        self.dr.get(URL.URL.admin_url(self))

    def config_Firefox(self):
        """打开火狐浏览器
        隐式等待为10秒"""
        self.dr = webdriver.Firefox()
        config.config(self)
        self.dr.get(URL.URL.admin_url(self))

