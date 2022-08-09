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
        if len(feature.feature_pack_list_api(create_data.name)) > 0:
            self.feature.delete_feature_pack_api(feature_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/119", name="新增功能包")
    def test_tenant_list(self):
        pass
