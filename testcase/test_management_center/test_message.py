import allure
from hamcrest import *

from apis.management_center.message_apis import Message
from case_data.management_center_data.message_data import MessageData


class TestMessage:
    def setup_class(self):
        self.message=Message()
        self.data=MessageData()



    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/55", name="开通媒介")
    def test_active_message_channel(self):
        res=self.message.active_message_channel_api("inbox")
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/55", name="媒介模板设置")
    def test_set_channel_of_message_templates(self):
        data=self.data.set_channel_of_message_templates_data()
        res=self.message.set_channel_of_message_templates_api(data)
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/58", name="编辑消息模板")
    def test_set_channels_of_message_template(self):
        data=self.data.set_channels_of_message_template_data()
        res=self.message.set_channels_of_message_template_api(data)
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/57", name="取消开通媒介")
    def test_deactivate_message_channel(self):
        res= self.message.deactivate_message_channel_api("inbox")
        assert_that(res,equal_to(True))

