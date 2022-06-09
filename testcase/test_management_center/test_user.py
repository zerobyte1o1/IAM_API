import allure
import pytest
from hamcrest import *

from apis.management_center.user_apis import User
from case_data.management_center_data.user_data import UserData


class TestUser:
    def setup(self):
        self.datadir = UserData()
        self.user = User()

    @pytest.fixture(scope="function")
    def pre_user(self):
        data = UserData().create_user()
        id = User().create_user(data).user_id
        yield id
        user_detail = self.user.get_user(id)
        if len(user_detail) != 0:
            self.user.disable_users([id])
            self.user.delete_users([id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/34", name="创建用户")
    def test_create_user(self):
        create_user_dict = self.datadir.create_user()
        res = self.user.create_user(create_user_dict)
        assert_that(type(res.password), equal_to(str))
        self.user.disable_users([res.user_id])
        self.user.delete_users([res.user_id])

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/35", name="查看用户详情")
    def test_update_user(self, pre_user):
        data = self.datadir.update_user(pre_user)
        res = self.user.update_user(data)
        assert_that(res, equal_to(True))


    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/36", name="重置用户密码")
    def test_reset_user_password(self, pre_user):
        res = self.user.reset_user_password(pre_user)
        assert_that(type(res), equal_to(str))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/37", name="禁用用户")
    def test_disable_users(self, pre_user):
        res = self.user.disable_users([pre_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/38", name="启用用户")
    def test_enable_users(self, pre_user):
        self.user.disable_users([pre_user])
        res = self.user.enable_users([pre_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/39", name="查看用户详情")
    def test_user(self, pre_user):
        res = self.user.get_user(pre_user)
        assert_that(res.account, starts_with("account"))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/41", name="删除用户")
    def test_delete_user(self, pre_user):
        self.user.disable_users([pre_user])
        res = self.user.delete_users([pre_user])
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/42", name="添加用户权限")
    def test_set_authorization_rules_to_user(self, pre_user):
        data = self.datadir.set_authorization_rules_to_user(pre_user)
        res = self.user.set_authorization_rules_to_user_api(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/43", name="删除用户权限")
    def test_remove_authorization_rules_of_user(self, pre_user):
        data = self.datadir.set_authorization_rules_to_user(pre_user)
        self.user.set_authorization_rules_to_user_api(data)
        rule_ids = self.datadir.get_direct_authorization_rules_id_of_user(pre_user)
        res = self.user.remove_authorization_rules_of_user_api(rule_ids, pre_user)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/44", name="修改用户权限")
    def test_update_update_authorization_rules_of_user(self, pre_user):
        data = self.datadir.set_authorization_rules_to_user(pre_user)
        self.user.set_authorization_rules_to_user_api(data)
        update_dict = UserData().update_authorization_rules_of_user(pre_user)
        res = self.user.update_authorization_rules_of_user_api(update_dict)
        assert_that(res, equal_to(True))
