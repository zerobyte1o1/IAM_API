import allure
import pytest
from hamcrest import *

from apis.platform_management.feature_pack import FeaturePack
from case_data.platform_management_data.feature_pack_data import FeaturePackData


class TestFeaturePack:
    def setup_class(self):
        self.feature = FeaturePack()
        self.feature_date = FeaturePackData()

    @pytest.fixture(scope="class")
    def pre_feature_pack(self):
        feature = FeaturePack()
        feature_data = FeaturePackData()
        create_data = feature_data.create_feature_pack_data()
        feature_id = feature.create_feature_pack_api(create_data)
        yield feature_id
        if feature.feature_pack_list_api(create_data["name"]).total_count > 0:
            self.feature.delete_feature_pack_api(feature_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/118", name="功能包列表")
    def test_feature_pack_list(self):
        res = self.feature.feature_pack_list_api()
        assert_that(len(res) > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/119", name="新增功能包")
    def test_create_feature_pack(self):
        data = self.feature_date.create_feature_pack_data()
        res = self.feature.create_feature_pack_api(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/120", name="编辑功能包")
    def test_update_feature_pack(self, pre_feature_pack):
        data = self.feature_date.update_feature_pack_data(pre_feature_pack)
        res = self.feature.update_feature_pack_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/122", name="配置功能点")
    def test_set_permissions_to_feature_pack(self, pre_feature_pack):
        res_assign = self.feature.assignable_permissions_of_tenant_api()
        assert_that(type(res_assign), equal_to(list))
        res_own_permission = self.feature.permissions_of_feature_packs_api(pre_feature_pack)
        assert_that(type(res_own_permission), equal_to(list))
        data = self.feature_date.set_permissions_to_feature_pack_data(pre_feature_pack)
        res = self.feature.set_permissions_to_feature_pack_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/123", name="查看功能包基本信息")
    def test_feature_pack(self,pre_feature_pack):
        res=self.feature.feature_pack_api(pre_feature_pack)
        assert_that("id" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/124", name="确认功能包")
    def test_confirm_feature_pack(self,pre_feature_pack):
        res=self.feature.confirm_feature_pack_api(pre_feature_pack)
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/121", name="删除功能包")
    def test_delete_feature_pack(self,pre_feature_pack):
        res=self.feature.delete_feature_pack_api(pre_feature_pack)
        assert_that(res,equal_to(True))

