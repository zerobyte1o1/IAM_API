from apis.platform_management.tenant_api import TenantApi
from case_data.platform_management_data.tenant_data import TenantData


class TestTenant:
    def setup(self):
        self.tenant = TenantApi()
        self.tenant_data = TenantData()







