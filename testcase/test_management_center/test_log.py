import allure
import pytest
from hamcrest import *

from apis.management_center.log_apis import Log
from case_data.management_center_data.log_data import LogData

class TestLog:
    def setup(self):
        self.log=Log()
        self.log_data=LogData()

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/59", name="日志默认查询")
    def test_log_list(self):
        data=self.log_data.get_log_list_filter(search="null")
        res=self.log.get_log_list(data)
        assert_that(len(res)>0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/60", name="日志筛选")
    def test_log_list_admin(self):
        data = self.log_data.get_log_list_filter()
        res = self.log.get_log_list(data)
        assert_that(len(res) > 0)
