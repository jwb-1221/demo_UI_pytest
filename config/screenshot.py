from PIL import ImageGrab
from config.config import *
class scrrrnshot(object):
    """截图对象"""
    def scrrrnshot(self,interface):
        """浏览器截图方法"""
        pic_path = (scrrrnshot_report+interface +".png")
        print(pic_path)
        time.sleep(2)
        self.dr.save_screenshot(pic_path)
    def ImageGrab(self,interface):
        """桌面窗口截图方法"""
        ImageGrab.grab().save(scrrrnshot_report+interface +".png")
        time.sleep(2)
