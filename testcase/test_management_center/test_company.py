from hamcrest import *
import allure
from apis.management_center.company_apis import Company
from apis.management_center.user_apis import User
from apis.platform_management.tenant_apis import Tenant
from case_data.management_center_data.user_data import UserData

from case_data.platform_management_data.tenant_data import TenantData


class TestCompany:
    def setup_class(self):
        # 创建并更换普通企业账号，并创建企业人员。
        self.tenant = Tenant()
        self.t_data = TenantData()
        self.u_data = UserData()
        tenant_create_data = self.t_data.create_tenant_ask()
        self.tenant_id = self.tenant.create_tenant_api(tenant_create_data)
        # 添加企业app
        tenant_app_data = self.t_data.assign_tenant_apps_ask(self.tenant_id)
        self.tenant.assign_tenant_apps_api(tenant_app_data)
        # 添加企业app权限
        tenant_permission_data = self.t_data.set_permissions_to_tenant_ask(self.tenant_id)
        self.tenant.set_permissions_to_tenant_api(tenant_permission_data)
        # 创建企业拥有者
        tenant_create_owner_data = self.t_data.create_tenant_owner_ask(self.tenant_id)
        owner = self.tenant.create_tenant_owner_api(tenant_create_owner_data)
        account = self.tenant.get_tenant(self.tenant_id).owner.account
        self.company = Company(account=account, password=owner.password, tenant_code=tenant_create_data["code"])
        self.user = User(account=account, password=owner.password, tenant_code=tenant_create_data["code"])
        # 创建企业用户
        user_create_data = self.u_data.create_user()
        self.n_user=self.user.create_user(user_create_data).user_id

    def teardown_class(self):
        tenant = Tenant()
        tenant.disable_tenant_api(self.tenant_id)
        tenant.delete_tenant_api(self.tenant_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/95", name="管理员列表")
    def test_admin_user_list(self):
        res=self.company.get_admin_user_list()
        assert_that(res.total_count > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/65", name="添加管理员")
    def test_set_admin_users(self):
        res=self.company.set_admin_users_api([self.n_user])
        assert_that(res,equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/66", name="删除管理员")
    def test_unset_admin_users(self):
        res = self.company.unset_admin_users_api([self.n_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/64", name="转移拥有者")
    def test_transfer_tenant_owner(self):
        res=self.company.transfer_tenant_owner_api(self.n_user)
        assert_that(res,equal_to(True))