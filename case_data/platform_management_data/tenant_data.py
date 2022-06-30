from apis.base.base_api import BaseApi
from apis.platform_management.tenant_apis import Tenant
from utils.mock import Mock


class TenantData(BaseApi):
    tenant = Tenant()
    mock = Mock()

    def create_tenant_ask(self):
        """

        @return: dict
        """
        industry_id=self.tenant.get_tenant_industry_tree_nodes()[0].id
        print(industry_id)
        variables_temp = self.get_variables(module_name="tenant", variables_name="create_tenant")
        args = [("address", self.faker.address()),
                ("code", self.faker.ean8()),
                ("email", self.faker.email()),
                ("name", self.faker.company()),
                ("phone", self.faker.phone_number()),
                ("uscc", self.faker.ean13()),
                ("industry",{"id":industry_id})]

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_tenant_ask(self, tenant_id):
        """
        更新企业的请求数据
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

        app_ids_added = self.tenant.get_tenant_app_list(tenant_id=tenant_id, args=["id", "name"])
        my_app_ids = self.tenant.get_my_tenant_app_list(args=["id", "name"])
        if "管理中心" not in [i["name"] for i in app_ids_added]:
            app_id = [i["id"] for i in my_app_ids if i["name"] == "管理中心"]
        else:
            app_id = [i["id"] for i in my_app_ids if i not in app_ids_added]
        variables = {"apps": [{"id": app_id[0]}], "tenant": {"id": tenant_id}}
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
        args = [("account", self.mock.mock_data("owner")),
                ("email", self.faker.email()),
                ("phoneNumber", self.faker.phone_number()),
                ("tenant", {"id": tenant_id})]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_permissions_to_tenant_ask(self, tenant_id):
        all_permissions = self.tenant.assignable_permissions_of_tenant_api(tenant_id)
        added_permissions = self.tenant.permissions_of_tenant_api(tenant_id)
        permission_id = [i for i in all_permissions if i not in added_permissions]
        variables = {
            "permissions": permission_id,
            "tenant": {"id": tenant_id}
        }
        return variables

    def add_meta_templates_to_tenant_ask(self, tenant_id):
        permission_id = self.tenant.get_assignable_meta_template_list_of_tenant(tenant_id)
        variables = {
            "ids": [permission_id],
            "tenantId": {"id": tenant_id}
        }
        return variables

    def delete_message_templates_of_tenant_ask(self, tenant_id):
        permission_id = self.tenant.get_message_template_list_of_tenant(tenant_id)
        variables = {
            "ids": [permission_id],
            "tenantId": {"id": tenant_id}
        }
        return variables


if __name__ == '__main__':
    td = TenantData()
    ta = Tenant()
    data = td.create_tenant_ask()
    print(data)
