from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Tenant(GetTokenHeader):

    def get_tenant_list(self, tenant_name=None):
        """
        企业列表，可用企业名称查询查询
        @param tenant_name: 企业名称
        @return: 返回企业列表
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.tenant_list(filter={'search': tenant_name})
        data = endpoint(op)
        res = (op + data).tenant_list.data
        return res

    def get_tenant_industry_tree_nodes(self):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.tenant_industry_tree_nodes()
        data = endpoint(op)
        res = (op + data).tenant_industry_tree_nodes
        return res

    def create_tenant_api(self, variables):
        """
        创建企业
        @param variables: 创建企业的请求数据
        @return: 返回企业id
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_tenant(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_tenant
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_tenant(self, tenant_id):
        """
        获取企业的详细信息
        @param tenant_id: 企业id
        @return: 返回企业信息
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.tenant(id=tenant_id)
        data = endpoint(op)
        res = (op + data).tenant
        return res

    def get_tenant_app_list(self, tenant_id, args=None):
        """
        获取企业已添加的app
        @param tenant_id: 企业id
        @param args: 筛选数据剩余内容【"id"】
        @return: 返回企业已添加的app
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        tenant_app_list = op.tenant_app_list(filter={"tenant": {"id": tenant_id}})
        if args:
            tenant_app_list.data.__fields__(*args)
        data = endpoint(op)
        res = (op + data).tenant_app_list.data
        return data["data"]["tenantAppList"]["data"]

    def get_my_tenant_app_list(self, args=None):
        """
        获取所有app
        @param args: 筛选返回内容 【"id"】
        @return: 返回所有app
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        my_tenant_app_list = op.my_tenant_app_list()
        if args:
            my_tenant_app_list.data.__fields__(*args)
        data = endpoint(op)
        res = (op + data).my_tenant_app_list.data
        return data["data"]["myTenantAppList"]["data"]

    def assign_tenant_apps_api(self, variables):
        """
        添加app
        @param variables:企业添加app的请求数据
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.assign_tenant_apps(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).assign_tenant_apps
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def un_assign_tenant_apps_api(self, variables):
        """
        删除app
        @param variables: 企业删除app的请求数据
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.un_assign_tenant_apps(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).un_assign_tenant_apps
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_tenant_owner_api(self, variables):
        """
        创建企业拥有者
        @param variables: 创建owner请求数据
        @return: password and userId
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)

        op.create_tenant_owner(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_tenant_owner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def reset_tenant_owner_password_api(self, **kwargs):
        """
        重置拥有者密码
        @param kwargs:tenant_id and user_id
        @return: 12位密码
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.reset_tenant_owner_password(
            tenant_id=kwargs["tenantId"],
            user_id=kwargs["userId"]
        )
        data = endpoint(op)
        try:
            res = (op + data).reset_tenant_owner_password
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_tenant_api(self, variables):
        """
        更新企业信息
        @param variables: 企业更新请求内容
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_tenant(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_tenant
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def disable_tenant_api(self, tenant_id):
        """
        禁用企业
        @param tenant_id: 企业id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.disable_tenant(id=tenant_id)
        data = endpoint(op)
        res = (op + data).disable_tenant
        return res

    def enable_tenant_api(self, tenant_id):
        """
        启用企业
        @param tenant_id: 企业id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.enable_tenant(id=tenant_id)
        data = endpoint(op)
        res = (op + data).enable_tenant
        return res

    def delete_tenant_api(self, tenant_id):
        """
        删除企业
        @param tenant_id: 企业id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_tenant(id=tenant_id)
        data = endpoint(op)
        res = (op + data).delete_tenant
        return res



    def permissions_of_tenant_api(self, tenant_id):
        """
        查询出企业已经添加的权限
        @param tenant_id: 企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        permissions_of_tenant = op.permissions_of_tenant(filter={"types": ["MENU"]},
                                                         tenant_id=tenant_id)
        permissions_of_tenant.__fields__("id")
        data = endpoint(op)
        return data["data"]["permissionsOfTenant"]

    def set_permissions_to_tenant_api(self, variables):
        """
        设置企业权限
        @param variables:已配置好的未添加的单一权限
        @return: Ture or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_permissions_to_tenant(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).set_permissions_to_tenant
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_assignable_meta_template_list_of_tenant(self, tenant_id):
        """
        获得一个可添加的应用模板
        @param tenant_id:企业id
        @return:返回一个模板id
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.assignable_meta_template_list_of_tenant(tenant_id=tenant_id)
        data = endpoint(op)
        res = (op + data).assignable_meta_template_list_of_tenant
        return res["data"][0].id

    def add_meta_templates_to_tenant_api(self, variables):
        """
        添加应用模板
        @param variables:
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.add_meta_templates_to_tenant(ids=variables["ids"],
                                        tenant_id=variables["tenantId"])
        data = endpoint(op)
        try:
            res = (op + data).add_meta_templates_to_tenant
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_message_template_list_of_tenant(self, tenant_id):
        """
        获取所有已添加的应用模板
        @param tenant_id:企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.message_template_list_of_tenant(tenant_id=tenant_id)
        data = endpoint(op)
        res = (op + data).message_template_list_of_tenant
        return res

    def delete_message_templates_of_tenant_api(self, variables):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_message_templates_of_tenant(ids=variables["ids"],
                                              tenant_id=variables["tenantId"])
        data = endpoint(op)
        res = (op + data).delete_message_templates_of_tenant
        return res

    def accept_tenant_certification_api(self, tenant_id):
        """
        通过认证
        @param tenant_id: 企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.accept_tenant_certification(id=tenant_id)
        data = endpoint(op)
        res = (op + data).accept_tenant_certification
        return res

    def reject_tenant_certification_api(self, tenant_id):
        """
        认证失败
        @param tenant_id: 企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.reject_tenant_certification(id=tenant_id,reason="不给予通过")
        data = endpoint(op)
        res = (op + data).reject_tenant_certification
        return res

if __name__ == '__main__':
    a = Tenant()

    res = a.create_tenant_owner_api("3d296cf6-2c7b-47ad-b349-3e7abc607b5b").owner
    print(res)
