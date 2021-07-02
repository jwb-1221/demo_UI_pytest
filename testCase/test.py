
import pytest

import allure

from common.browser import config

class Testcase(object):
    def setup_class(self):
        print("类级别的 setup")
        config.config_Chrome_admin(self)
    def teardown_class(self):
        print("类级别的teardown")

    def setup_method(self):
        print('类方法级别的 setup.....')
    def teardown_method(self):
        print('类方法级别的 teardown.....')
    # @pytest.mark.skip(condition='我就是要跳过这个用例啦')
    @allure.title('测试用例标题1')
    @allure.description('这是测试用例用例1的描述信息')
    def test_case01(self):

        print('执行用例01.......')

        assert 0  # 断言失败

    # @pytest.mark.skipif(condition=1<2, reason='如果条件为true就跳过用例')
    @allure.title('测试用例标题2')
    @allure.description('这是测试用例用例2的描述信息')
    def test_case02(self):
        print('执行用例02.......')

        assert 1  # 断言成功




if __name__ == '__main__':

    pytest.main(["-s", "test.py"])
