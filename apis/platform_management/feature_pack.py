from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class FeaturePack(GetTokenHeader):
    def tenant_industry_tree_nodes_api(self):
        """
        获取所有行业
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.tenant_industry_tree_nodes()
        data = endpoint(op)
        res = (op + data).tenant_industry_tree_nodes
        return res

    def app_groups_api(self):
        """
        获取所有app的id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.app_groups()
        data = endpoint(op)
        res = (op + data).app_groups
        return res

    def feature_pack_list_api(self,search=None):
        """
        获取功能包列表
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.feature_pack_list(filter={"search": search})
        data = endpoint(op)
        res = (op + data).feature_pack_list
        return res

    def create_feature_pack_api(self, input_data):
        """
        创建功能包
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_feature_pack(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).create_feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def udpate_feature_pack_api(self, input_data):
        """
        更新功能包
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.udpate_feature_pack(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).udpate_feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def delete_feature_pack_api(self, feature_id):
        """
        删除功能包
        @param feature_id:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_feature_pack(id=feature_id)
        data = endpoint(op)
        try:
            res = (op + data).delete_feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def confirm_feature_pack_api(self, feature_id):
        """
        确认功能包
        @param feature_id:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.confirm_feature_pack(id=feature_id)
        data = endpoint(op)
        try:
            res = (op + data).confirm_feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def feature_pack_api(self, feature_id):
        """
        查看功能包详情
        @param feature_id:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.feature_pack(id=feature_id)
        data = endpoint(op)
        try:
            res = (op + data).feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def assignable_permissions_of_tenant_api(self, tenant_id):
        """
        查询出所有企业可以被添加的权限
        @param tenant_id: 企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        assignable_permissions_of_tenant = \
        op.assignable_permissions_of_tenant(
            filter={"excludeAppKeys":self.app_groups_api()[-1].app_ids[-2:],
                    "types": ["MENU"]},
            tenant_id=tenant_id)
        assignable_permissions_of_tenant.__fields__("id")
        data = endpoint(op)
        return data["data"]["assignablePermissionsOfTenant"]

    def set_permissions_to_feature_pack_api(self,data):
        """
        配置功能包权限
        @param data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_permissions_to_feature_pack(input=data)
        data = endpoint(op)
        try:
            res = (op + data).set_permissions_to_feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res