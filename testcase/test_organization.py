import allure
import pytest
from hamcrest import *

from apis.management_center.organization_apis import Organization
from case_data.organization_data import OrganizationData


class TestOrganization():
    def setup(self):
        self.org = Organization()
        self.data = OrganizationData()

    @pytest.fixture(scope="class")
    def pre_org(self):
        org = Organization()
        data = OrganizationData()
        data_create_org = data.create_organization_ask()
        org_id = org.create_organization_api(data_create_org)
        yield org_id
        org.delete_organization_api(org_id)

    def test_get_organization_list(self, pre_org):
        ask_data=self.data.get_organization_list_ask()
        org_lists=self.org.get_organization_list(ask_data)
        print(org_lists)
