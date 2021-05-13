from selenium import webdriver
from config import URL
class config():
    """浏览器类"""
    def __init__(self):
        self.dr =None
    def config(self):
        "配置浏览器信息"
        self.dr.implicitly_wait(5)
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

