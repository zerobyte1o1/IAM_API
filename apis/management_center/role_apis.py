from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Role(GetTokenHeader):
    def get_role_list(self, args=None, **kwargs):
        """
        获取角色列表
        @param args:list [""]
        @param kwargs: dict
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        users_info = op.role_list(
            filter=eval(f"{kwargs}")
        )
        if args:
            users_info.data.__fields__(*args)
        data = endpoint(op)
        res = (op + data).role_list
        return res

    def create_role(self, variables):
        """
        创建角色
        @param variables: dict
        """

        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_role(self, variables):
        """
        更新角色的基础信息
        @param variables: dict
        """

        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_role(self, ids):
        """
        删除角色
        @param ids:[list]
        @return: True or False
        """

        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_role(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def set_authorization_rules_to_role_api(self, variables: dict):
        """
        为用户添加权限规则
        @param variables:dict
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_authorization_rules_to_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).set_authorization_rules_to_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def role_exist(self, role_id):
        """
        判断角色是否存在
        @param role_id: 被判断的角色id
        @return: True or False
        """
        data = self.get_role_list(args=["id"]).data
        flags = False
        for i in range(len(data)):
            if data[i].id == role_id:
                flags = True
                break
        return flags

    def set_role_accounts_api(self, input_data):
        """
        为角色批量设置账号
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_role_accounts(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).set_role_accounts
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def all_authorization_roles_of_role_api(self, args=None, **kwargs):
        """
        获取角色下所有权限详情
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        all_authorization_rules_of_role = op.all_authorization_rules_of_role(filter=kwargs["filter"],
                                                                             role_id=kwargs["role_id"])
        if args:
            all_authorization_rules_of_role.__fields__(*args)
        data = endpoint(op)
        return data["data"]["allAuthorizationRulesOfRole"]

    def update_authorization_rule_api(self, input_data):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_authorization_rule(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).update_authorization_rule
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    role = Role()
