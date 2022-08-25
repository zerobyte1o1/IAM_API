import allure
import pytest
from hamcrest import *

from apis.management_center.account_apis import Account
from case_data.management_center_data.account_data import AccountData
from apis.management_center.staff_apis import Staff
from case_data.management_center_data.staff_data import StaffData


class TestAccount:
    def setup_class(self):
        self.account = Account()
        self.staff = Staff()
        self.staff_data = StaffData()
        self.account_data = AccountData()

    @pytest.fixture(scope="class")
    def pre_account(self):
        staff = Staff()
        staff_data = StaffData()
        create_staff_data = staff_data.create_staff_data()
        staff_id = staff.create_staff_apis(create_staff_data)
        create_account_data = staff_data.create_account_data(staff_id)
        account_id = staff.create_account_apis(create_account_data).account_id
        yield account_id
        account_list_data = self.account_data.account_list_filter(create_account_data["account"])
        count = self.account.get_account_list(account_list_data).total_count
        if count > 0:
            self.staff.resign_staff_apis(staff_id)
            self.staff.delete_staff_apis(staff_id)

    def test_01(self, pre_account):
        pass

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/106", name="查看账号列表")
    def test_account_list(self):
        account_list_data = self.account_data.account_list_filter()
        res = self.account.get_account_list(account_list_data)
        assert_that("data" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/107", name="查看账号详情")
    def test_account(self, pre_account):
        res = self.account.account_api(pre_account)
        assert_that("account" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/108", name="重置密码")
    def test_reset_account_password(self, pre_account):
        res = self.account.reset_account_password_api(pre_account)
        assert_that(len(res) == 12)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/129", name="批量分配角色")
    def test_add_account_roles(self, pre_account):
        data = self.account_data.add_and_remove_account_roles_data(pre_account)
        res = self.account.add_account_roles_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/130", name="批量移除角色")
    def test_remove_account_roles(self, pre_account):
        data = self.account_data.add_and_remove_account_roles_data(pre_account)
        res = self.account.remove_account_roles_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/130", name="批量移除角色")
    def test_set_authorization_roles_to_user(self, pre_account):
        staff_id = self.account.account_api(pre_account).staff.id
        data = self.account_data.set_authorization_rules_to_user(staff_id)
        res = self.account.set_authorization_rules_to_user_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/107", name="权限概览")
    def test_all_authorizations_of_user(self, pre_account):
        staff_id = self.account.account_api(pre_account).staff.id
        res = self.account.all_authorizations_of_user_api(staff_id)
        print(res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/116", name="添加功能权限")
    def test_set_authorization_roles_to_user(self,pre_account):
        staff_id = self.account.account_api(pre_account).staff.id
        data=self.account_data.set_authorization_rules_to_user(staff_id)
        res=self.account.set_authorization_rules_to_user_api(data)
        print(res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/110", name="禁用账号")
    def test_update_account_disable(self, pre_account):
        data = self.account_data.update_account_data(pre_account, False)
        res = self.account.update_account_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/107", name="启用账号")
    def test_update_account_able(self, pre_account):
        data = self.account_data.update_account_data(pre_account, True)
        res = self.account.update_account_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/112", name="删除账号")
    def test_delete_account(self, pre_account):
        res = self.account.delete_account_api(pre_account)
        assert_that(res, equal_to(True))
