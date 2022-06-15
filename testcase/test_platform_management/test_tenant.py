import allure
import pytest
from hamcrest import *

from apis.platform_management.tenant_api import TenantApi
from case_data.platform_management_data.tenant_data import TenantData


class TestTenant:
    def setup(self):
        self.tenant = TenantApi()
        self.tenant_data = TenantData()

    @pytest.fixture(scope="class")
    def pre_tenant(self):
        tenant = TenantApi()
        tenant_data = TenantData()
        create_data = tenant_data.create_tenant_ask()
        tenant_id = tenant.create_tenant_api(create_data)
        yield tenant_id
        if len(tenant.get_tenant(tenant_id)) > 0:
            tenant.disable_tenant_api(tenant_id)
            tenant.delete_tenant_api(tenant_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/72", name="企业列表")
    def test_tenant_list(self, pre_tenant):
        res = self.tenant.get_tenant_list()
        assert_that(len(res) > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/73", name="查看企业详情")
    def test_tenant(self, pre_tenant):
        res = self.tenant.get_tenant(pre_tenant)
        assert_that(res["id"], equal_to(pre_tenant))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/73", name="企业订阅app")
    def test_assign_tenant_apps(self, pre_tenant):
        data = self.tenant_data.assign_tenant_apps_ask(pre_tenant)
        res = self.tenant.assign_tenant_apps_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/74", name="企业删除app")
    def test_un_assign_tenant_apps(self, pre_tenant):
        data = self.tenant_data.un_assign_tenant_apps_ask(pre_tenant)
        res = self.tenant.un_assign_tenant_apps_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/76", name="创建拥有者")
    def test_create_tenant_owner(self, pre_tenant):
        data = self.tenant_data.create_tenant_owner_ask(pre_tenant)
        res = self.tenant.create_tenant_owner_api(data)
        assert_that(len(res["password"]), equal_to(12))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/77", name="重置拥有者密码")
    def test_reset_tenant_owner_password(self, pre_tenant):
        user_id = self.tenant.get_tenant(pre_tenant)["owner"]["id"]
        res = self.tenant.reset_tenant_owner_password_api(tenantId=pre_tenant, userId=user_id)
        assert_that(len(res), equal_to(12))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/79", name="编辑企业")
    def test_update_tenant(self, pre_tenant):
        data = self.tenant_data.update_tenant_ask(pre_tenant)
        res = self.tenant.update_tenant_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/80", name="禁用企业")
    def test_disable_tenant(self, pre_tenant):
        res = self.tenant.disable_tenant_api(pre_tenant)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/81", name="启用企业")
    def test_enable_tenant(self, pre_tenant):
        res = self.tenant.enable_tenant_api(pre_tenant)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/82", name="删除企业")
    def test_delete_tenant(self, pre_tenant):
        res = self.tenant.delete_tenant_api(pre_tenant)
        assert_that(res, equal_to(True))
