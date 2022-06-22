from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Company(GetTokenHeader):
    def __init__(self, **kwargs):
        super().__init__()
        if kwargs:
            self.headers = self.get_headers(account=kwargs["account"], password=kwargs["password"], tenant_code=kwargs["tenant_code"])
        else:
            self.headers=self.get_headers()

    def get_admin_user_list(self):
        """
        获取管理员列表
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.admin_user_list()
        data = endpoint(op)
        res = (op + data).admin_user_list
        return res

    def set_admin_users_api(self, ids):
        """
        设置普通用户为管理员
        @param ids:[list]
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_admin_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).set_admin_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def unset_admin_users_api(self, ids):
        """
        移除管理员
        @param ids:[list]
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.unset_admin_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).unset_admin_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def transfer_tenant_owner_api(self, targetUserId):
        """
        转移企业拥有者
        @param targetUserId:
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.transfer_tenant_owner(target_user_id=targetUserId)
        data = endpoint(op)
        try:
            res = (op + data).transfer_tenant_owner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res
