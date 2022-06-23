import allure
import pytest
from hamcrest import *

from apis.management_center.authentication_apis import Authentication
from case_data.management_center_data.authentication_data import AuthenticationData


class TestAuthentication:
    def setup_class(self):
        self.au = Authentication()
        self.au_data = AuthenticationData()

    @pytest.fixture(scope="function")
    def pre_auth(self):
        au = Authentication()
        au_data = AuthenticationData()
        res = au.authentication_configuration_api()
        if "id" not in res:
            create_data = au_data.get_oauth2_ask()
            au.create_oauth2_authentication_configuration_api(create_data)
            res = au.authentication_configuration_api()
        yield res["id"]
        if len(au.authentication_configuration_api()) != 0:
            au.delete_authentication_configuration_api(res["id"])

    @pytest.fixture(scope="function")
    def pre_oidc(self):
        au = Authentication()
        au_data = AuthenticationData()
        res = au.authentication_configuration_api()
        if "id" not in res:
            create_data = au_data.get_oidc1_ask()
            au.create_open_idconnect1_authentication_configuration_api(create_data)
            res = au.authentication_configuration_api()
        yield res["id"]
        if len(au.authentication_configuration_api()) != 0:
            au.delete_authentication_configuration_api(res["id"])



    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/68", name="创建OAUTH2.0认证")
    def test_create_oauth2_authentication_configuration(self):
        create_data = self.au_data.get_oauth2_ask()
        res = self.au.create_oauth2_authentication_configuration_api(create_data)
        assert_that("-" in res)
        au_id = self.au.authentication_configuration_api()["id"]
        self.au.delete_authentication_configuration_api(au_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/69", name="创建OIDC1.0认证")
    def test_create_open_idconnect1_authentication_configuration(self):
        create_data = self.au_data.get_oidc1_ask()
        res = self.au.create_open_idconnect1_authentication_configuration_api(create_data)
        assert_that(type(res), equal_to(str))
        au_id = self.au.authentication_configuration_api()["id"]
        self.au.delete_authentication_configuration_api(au_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/70", name="更新OAUTH2.0认证")
    def test_update_oauth2_authentication_configuration(self, pre_auth):
        update_data = self.au_data.get_oauth2_ask(pre_auth)
        res = self.au.update_oauth2_authentication_configuration_api(update_data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/71", name="更新OIDC1.0认证")
    def test_update_open_idconnect1_authentication_configuration(self, pre_oidc):
        update_data = self.au_data.get_oidc1_ask(pre_oidc)
        res = self.au.update_open_idconnect1_authentication_configuration_api(update_data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/67", name="重置认证")
    def test_delete_authentication_configuration(self, pre_auth):
        res = self.au.delete_authentication_configuration_api(pre_auth)
        assert_that(res, equal_to(True))