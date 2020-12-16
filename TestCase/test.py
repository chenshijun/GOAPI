import allure
import pytest
from pytest_testconfig import config

from TestData.function1 import *
from util.Api import BaseRequest
from util.Logger import Logger

log = Logger().get_log()


@allure.feature("测试样例")
class TestClassDemo:

    @pytest.mark.parametrize('url', get_url(), ids=[""])
    @pytest.mark.parametrize('data', get_data(), ids=[x['desc'] for x in get_data()])
    # @allure.title("{data[desc]}")
    def test_api(self, url, data):
        server = BaseRequest(config['gHub']['default'], url, data=data['data'])
        result = server.post()
        allure.attach(name='接口的返回结果', body=result.response_text)
        log.info("this is a test log")
        assert result.response_json['code'] == "500"

    @allure.title("成功用例")
    def test_info(self):
        assert True
