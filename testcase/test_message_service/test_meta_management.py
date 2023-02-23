import random

import allure
import pytest
from hamcrest import *

from apis.message_service.media_management_api import MediaManagement
from case_data.message_service.media_management_data import MediaManagementData


class TestMetaManagement:
    def setup_class(self):
        self.data = MediaManagementData()
        self.media_management = MediaManagement()

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/92", name="媒介内容")
    def test_get_meta_channels(self):
        res = self.media_management.get_meta_channels()
        assert_that(len(res), equal_to(3))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/93", name="编辑介绍")
    def test_update_meta_channel(self):
        meta_id = self.media_management.get_meta_channels()[random.randint(0, 2)].id
        meta_data = self.data.update_meta_channel_ask(meta_id)
        res = self.media_management.update_meta_channel_api(meta_data)
        assert_that(res, equal_to(True))
