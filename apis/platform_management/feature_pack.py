from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *
from apis.management_center.account_apis import User


class FeaturePack(GetTokenHeader):
    user = User()
    tenant_id = user.get_me().tenant.id

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

    def feature_pack_list_api(self, search=None):
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

    def update_feature_pack_api(self, input_data):
        """
        更新功能包
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_feature_pack(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).update_feature_pack
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
        op = Operation(Query)
        op.feature_pack(id=feature_id)
        data = endpoint(op)
        try:
            res = (op + data).feature_pack
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def assignable_permissions_of_tenant_api(self):
        """
        查询出所有企业可以被添加的权限
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        assignable_permissions_of_tenant = \
            op.assignable_permissions_of_tenant(
                filter={"excludeAppKeys": self.app_groups_api()[-1].app_ids[-2:],
                        "types": ["MENU"]},
                tenant_id=self.tenant_id)
        assignable_permissions_of_tenant.__fields__("id")
        data = endpoint(op)
        return data["data"]["assignablePermissionsOfTenant"]

    def set_permissions_to_feature_pack_api(self, data):
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

    def permissions_of_feature_packs_api(self, feature_id):
        """
        查询出功能包已经添加的权限
        @param tenant_id: 企业id
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.permissions_of_feature_packs(filter={"types": ["MENU", "PAGE"]},
                                        feature_pack_ids=[feature_id])

        data = endpoint(op)
        res=(op + data).permissions_of_feature_packs
        return res


if __name__ == '__main__':
    a = FeaturePack()
    res = a.permissions_of_feature_packs_api("24a3b856-a24a-42db-8ceb-51d368de2616")
    print(res)
