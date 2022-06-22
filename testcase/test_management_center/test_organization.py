import allure
import pytest
from hamcrest import *

from apis.management_center.organization_apis import Organization
from case_data.management_center_data.organization_data import OrganizationData


class TestOrganization:
    def setup_class(self):
        self.org = Organization()
        self.data = OrganizationData()

    @pytest.fixture(scope="function")
    def pre_org(self):
        org = Organization()
        data = OrganizationData()
        data_create_org = data.create_organization_ask()
        org_id = org.create_organization_api(data_create_org)
        yield org_id
        org_data = data.get_organization_list_ask(org_id)
        if org.get_organization_list(org_data).total_count != 0:
            org.delete_organization_api(org_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/45", name="查看组织列表")
    def test_get_organization_list(self, pre_org):
        ask_data = self.data.get_organization_list_ask()
        org_lists = self.org.get_organization_list(ask_data)
        assert_that(org_lists.total_count > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/46", name="添加组织")
    def test_create_organization(self):
        data_create_org = self.data.create_organization_ask()
        org_id = self.org.create_organization_api(data_create_org)
        assert_that('-' in org_id)
        self.org.delete_organization_api(org_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/47", name="修改组织")
    def test_update_organization(self, pre_org):
        org_data = self.data.update_organization_ask(pre_org)
        res = self.org.update_organization_api(org_data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/48", name="删除组织")
    def test_delete_organization(self, pre_org):
        res = self.org.delete_organization_api(pre_org)
        assert_that(res, equal_to(True))
