import allure
import pytest
from hamcrest import *

from apis.management_center.role_apis import Role
from case_data.management_center_data.role_data import RoleData


class TestRole:

    def setup(self):
        self.role = Role()
        self.data = RoleData()

    @pytest.fixture(scope="function")
    def pre_role(self):
        create_data = RoleData().create_role_ask()
        role_id = Role().create_role(create_data)
        yield role_id
        if self.role.role_exist(role_id):
            self.role.delete_role([role_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/50", name="创建角色")
    def test_create_role(self):
        data_create = self.data.create_role_ask()
        role_id = self.role.create_role(data_create)
        assert_info = self.role.role_exist(role_id)
        assert_that(assert_info, equal_to(True))
        self.role.delete_role([role_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/51", name="更新角色")
    def test_update_role(self, pre_role):
        data_update = self.data.update_role_ask(pre_role)
        res = self.role.update_role(data_update)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/52", name="删除角色")
    def test_delete_role(self, pre_role):
        res = self.role.delete_role([pre_role])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/54", name="查看权限列表")
    def test_role_list(self):
        res = self.role.get_role_list()
        assert_that(len(res) > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/53", name="权限配置")
    def test_set_authorization_roles_to_role(self,pre_role):
        data_set=self.data.set_authorization_rules_to_role(pre_role)
        res=self.role.set_authorization_rules_to_role_api(data_set)
        assert_that(res,equal_to(True))