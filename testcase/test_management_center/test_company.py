from hamcrest import *
import allure
from apis.management_center.company_apis import Company
from apis.platform_management.tenant_apis import Tenant
from apis.management_center.staff_apis import Staff
from apis.platform_management.feature_pack import FeaturePack
from case_data.management_center_data.staff_data import StaffData
from case_data.platform_management_data.tenant_data import TenantData
from case_data.platform_management_data.feature_pack_data import FeaturePackData


class TestCompany:
    def setup_class(self):
        # 创建并更换普通企业账号，并创建企业人员。
        self.tenant = Tenant()
        self.feature = FeaturePack()
        self.t_data = TenantData()
        self.s_data = StaffData()
        self.f_data = FeaturePackData()
        tenant_create_data = self.t_data.create_tenant_ask()
        self.tenant_id = self.tenant.create_tenant_api(tenant_create_data)
        # 添加企业app
        tenant_app_data = self.t_data.assign_tenant_apps_ask(self.tenant_id)
        self.tenant.assign_tenant_apps_api(tenant_app_data)
        # 添加企业功能包
        self.feature_id=self.feature.create_feature_pack_api(self.f_data.create_feature_pack_data())
        self.feature.set_permissions_to_feature_pack_api(self.f_data.set_permissions_to_feature_pack_data(self.feature_id))
        self.feature.confirm_feature_pack_api(self.feature_id)

        # 创建企业拥有者
        tenant_create_owner_data = self.t_data.create_tenant_owner_ask(self.tenant_id)
        owner = self.tenant.create_tenant_owner_api(tenant_create_owner_data)
        account = self.tenant.get_tenant(self.tenant_id).owner.account
        self.company = Company(account=account, password=owner.password, tenant_code=tenant_create_data["code"])
        self.staff = Staff(account=account, password=owner.password, tenant_code=tenant_create_data["code"])
        # 认证租户
        self.company.apply_for_tenant_certification_api("159")
        self.tenant.accept_tenant_certification_api(self.tenant_id)
        # 创建企业用户
        staff_create_data = self.s_data.create_staff_data()
        staff_id = self.staff.create_staff_apis(staff_create_data)
        staff_create_account_data = self.s_data.create_staff_account_data(staff_id)
        self.n_user = self.staff.create_staff_account_apis(staff_create_account_data)

    # def teardown_class(self):
    #     tenant = Tenant()
    #     tenant.disable_tenant_api(self.tenant_id)
    #     tenant.delete_tenant_api(self.tenant_id)
    #     self.feature.delete_feature_pack_api(self.feature_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/95", name="管理员列表")
    def test_admin_account_list(self):
        res = self.company.get_admin_account_list()
        print(res)
        assert_that(res.total_count > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/65", name="添加管理员")
    def test_set_admin_users(self):
        res = self.company.set_admin_users_api([self.n_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/66", name="删除管理员")
    def test_unset_admin_users(self):
        res = self.company.unset_admin_users_api([self.n_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/64", name="转移拥有者")
    def test_transfer_tenant_owner(self):
        res = self.company.transfer_tenant_owner_api(self.n_user)
        assert_that(res, equal_to(True))
