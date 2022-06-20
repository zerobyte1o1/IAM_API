import allure
import pytest
from hamcrest import *

from apis.message_service.meta_template_apis import MetaTemplate
from case_data.message_service.meta_template_data import MetaTemplateData


class TestMetaTemplate:
    def setup(self):
        self.meta_template = MetaTemplate()
        self.data = MetaTemplateData()

    @pytest.fixture(scope="class")
    def pre_template(self):
        data = MetaTemplateData()
        meta_template = MetaTemplate()
        template_date = data.create_meta_template_ask()
        template_id = meta_template.create_meta_template_api(template_date)
        yield template_id
        try:
            meta_template.update_status_of_template_api(template_id, "DISABLED")
            meta_template.delete_meta_template_api(template_id)
        except ValueError:
            pass

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/86", name="创建模板")
    def test_create_meta_template_api(self):
        template_date = self.data.create_meta_template_ask()
        res = self.meta_template.create_meta_template_api(template_date)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/85", name="查看推送模板列表")
    def test_get_meta_template_list(self):
        res = self.meta_template.get_meta_template_list()
        assert_that(res.total_count > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/87", name="编辑模板")
    def test_update_meta_template_api(self, pre_template):
        template_date = self.data.update_meta_template_ask(pre_template)
        res = self.meta_template.update_meta_template_api(template_date)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/88", name="更新模板")
    def test_overwrite_message_template_api(self, pre_template):
        res = self.meta_template.overwrite_message_template_api(pre_template)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/90", name="禁用模板")
    def test_close_status_of_template_api(self, pre_template):
        res = self.meta_template.update_status_of_template_api(pre_template, "DISABLED")
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/89", name="启用模板")
    def test_open_status_of_template_api(self, pre_template):
        res = self.meta_template.update_status_of_template_api(pre_template, "ENABLED")
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/91", name="删除推送模板")
    def test_delete_meta_template_api(self, pre_template):
        res = self.meta_template.delete_meta_template_api(pre_template)
        assert_that(res, equal_to(True))
