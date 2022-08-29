import allure
import pytest
from hamcrest import *

from apis.management_center.staff_apis import Staff
from case_data.management_center_data.staff_data import StaffData


class TestStaff:

    def setup_class(self):
        self.staff_data = StaffData()
        self.staff = Staff()

    @pytest.fixture(scope="class")
    def pre_staff(self):
        data = StaffData().create_staff_data()
        staff_id = Staff().create_staff_apis(data)
        yield staff_id
        staff_list_data = self.staff_data.staff_list_data()
        staff_list = self.staff.get_staff_list(staff_list_data)
        if staff_id in str(staff_list):
            self.staff.delete_staff_apis(staff_id)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/96", name="人员列表")
    def test_staff_list(self):
        data = self.staff_data.staff_list_data()
        res = self.staff.get_staff_list(data)
        assert_that(res.total_count > 0)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/97", name="创建人员")
    def test_create_staff(self):
        data = self.staff_data.create_staff_data()
        res = self.staff.create_staff_apis(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/98", name="编辑人员")
    def test_update_staff(self, pre_staff):
        data = self.staff_data.update_staff_data(pre_staff)
        res = self.staff.update_staff_apis(data)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/101", name="办理离职")
    def test_resign_staff(self, pre_staff):
        res = self.staff.resign_staff_apis(pre_staff)
        assert_that(res, equal_to(True))


    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/102", name="重新入职")
    def test_rehire_staff(self, pre_staff):
        res = self.staff.rehire_staff_apis(pre_staff)
        assert_that(res, equal_to(True))

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/105", name="创建账号")
    def test_create_account(self, pre_staff):
        data = self.staff_data.create_account_data(pre_staff)
        res = self.staff.create_account_apis(data)
        assert_that("-" in res)

    @allure.testcase(url="https://teletraan.coding.net/p/auto/testing/cases/99", name="删除人员")
    def test_delete_staff(self, pre_staff):
        res = self.staff.delete_staff_apis(pre_staff)
        assert_that(res, equal_to(True))
