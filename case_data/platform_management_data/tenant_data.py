from apis.base.base_api import BaseApi
from apis.platform_management.tenant_api import TenantApi


class TenantData(BaseApi):
    tenant = TenantApi()

    def create_tenant_ask(self):
        """

        @return: dict
        """
        variables_temp = self.get_variables(module_name="tenant", variables_name="create_tenant")
        args = [("address", self.faker.address()),
                ("code", self.faker.ean8()),
                ("email", self.faker.email()),
                ("name", self.faker.company()),
                ("phone", self.faker.phone_number()),
                ("uscc", self.faker.ean13())]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_tenant_ask(self, tenant_id):
        """

        @param tenant_id: 企业id
        @return: dict
        """
        variables_temp = self.get_variables(module_name="tenant", variables_name="update_tenant")
        args = [("address", self.faker.address()),
                ("email", self.faker.email()),
                ("name", self.faker.company()),
                ("phone", self.faker.phone_number()),
                ("uscc", self.faker.ean13()),
                ("id", tenant_id)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def assign_tenant_apps_ask(self, tenant_id):
        """
        添加app的请求
        @param tenant_id: 企业id
        @return: dict
        """
        app_ids_added = self.tenant.get_tenant_app_list(tenant_id=tenant_id, args=["id"])
        my_app_ids = self.tenant.get_my_tenant_app_list(args=["id"])
        app_id = [i for i in my_app_ids if i not in app_ids_added]
        variables = {"apps": [{"id": app_id[0]["id"]}], "tenant": {"id": tenant_id}}
        return variables

    def un_assign_tenant_apps_ask(self, tenant_id):
        """
        删除app的请求
        @param tenant_id: 企业id
        @return: dict
        """
        app_id_added = self.tenant.get_tenant_app_list(tenant_id=tenant_id, args=["id"])[0]["id"]
        variables = {"apps": [{"id": app_id_added}], "tenant": {"id": tenant_id}}
        return variables

    def create_tenant_owner_ask(self, tenant_id):
        """
        创建企业拥有者请求
        @param tenant_id: 企业id
        @return: dict
        """
        variables_temp = self.get_variables(module_name="tenant", variables_name="create_tenant_owner")
        args = [("account", self.faker.name()),
                ("email", self.faker.email()),
                ("phoneNumber", self.faker.phone_number()),
                ("tenant", {"id": tenant_id})]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    td = TenantData()
    ta = TenantApi()
    data = td.create_tenant_owner_ask("5d9730b6-7e75-4a22-8b00-9b088e4d7fea")
    print(data)
    res = ta.create_tenant_owner_api(data)
    print(res)
