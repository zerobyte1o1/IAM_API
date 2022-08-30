from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Account(GetTokenHeader):
    def get_me(self):
        """
        :return:class User; 如果想要tcompany_id, 可以使用:
            res.company.id, res = return
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.me()
        data = endpoint(op)
        res = (op + data).me
        return res

    def account_api(self, account_id):
        """
        获取account基本信息
        @param account_id : account_id
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.account(id=account_id)
        data = endpoint(op)
        res = (op + data).account
        return res

    def get_account_list(self, variables):
        """
        获取用户列表数据
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.account_list(filter=variables)
        data = endpoint(op)
        res = (op + data).account_list
        return res

    def enable_accounts_apis(self, ids: list):
        """
        启用账号
        @param ids:list
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.enable_accounts(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).enable_accounts
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def disable_accounts_apis(self, id):
        """
        禁用账号
        @param ids : list
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.disable_accounts(ids=[id])
        data = endpoint(op)
        try:
            res = (op + data).disable_accounts
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_account_api(self, ids):
        """
        删除账号
        @param ids: 账号id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_account(ids=[ids])
        data = endpoint(op)
        try:
            res = (op + data).delete_account
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def reset_account_password_api(self, id: str):
        """
        重置用户密码
        @param id:用户id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.reset_account_password(id=id)
        data = endpoint(op)
        try:
            res = (op + data).reset_account_password
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_account_api(self, variables: dict):
        """
        更新账号，角色和登录状态
        @param variables: 更新账号请求数据
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_account(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_account
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_permissions(self, args=None, **kwargs):
        """
        获取已添加规
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        permissions = op.permissions(
            filter=eval(f"{kwargs}")
        )
        if args:
            permissions.__fields__(*args)
        data = endpoint(op)
        res = (op + data).permissions
        return res

    def get_all_permissions_of_user(self, args=None, **kwargs):
        """
        获取用户能够获得的所有权限信息
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        all_permissions_of_user = op.all_permissions_of_user(
            filter=eval(f"{kwargs['kwargs']['filter']}"),
            user_id=kwargs['kwargs']['userId']
        )
        if args:
            all_permissions_of_user.__fields__(*args)
        data = endpoint(op)
        res = (op + data).all_permissions_of_user
        return res

    def get_direct_authorization_rules_of_user(self, args=None, **kwargs):

        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        direct_authorization_rules_of_user = op.direct_authorization_rules_of_user(
            filter=eval(f"{kwargs['kwargs']['filter']}"),
            user_id=kwargs['kwargs']['userId']
        )
        if args:
            direct_authorization_rules_of_user.data.__fields__(*args)
            direct_authorization_rules_of_user.total_count()

        data = endpoint(op)
        res = (op + data).direct_authorization_rules_of_user
        return res

    def set_authorization_rules_to_user_api(self, variables: dict):
        """
        为用户添加权限规则
        @param variables:dict
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_authorization_rules_to_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).set_authorization_rules_to_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def remove_authorization_rules_of_user_api(self, ids: list, userId: str):
        """
        删除用户的一条权限规则
        @param ids:[list] rules id
        @param userId:[str] function_script id
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.remove_authorization_rules_of_user(ids=ids, user_id=userId)
        data = endpoint(op)
        try:
            res = (op + data).remove_authorization_rules_of_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_authorization_rules_of_user_api(self, variables: dict):
        """
        更新用户的一条权限规则
        @param variables:更新用户请求数据
        @return: True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_authorization_rules_of_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_authorization_rules_of_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def get_authorization_rule_and_dependencies(self, rule_id):
        """
        获取一条规则的详细数据
        @param rule_id:已添加规则id
        @return: True or False

        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.authorization_rule_and_dependencies(id=rule_id)
        data = endpoint(op)
        res = (op + data).authorization_rule_and_dependencies
        return res

    def ordinary_staff_app_list_of_my_tenant_api(self, staff_id):
        """
        获取该人员已有的所有appid
        @param staff_id:人员id
        @return: 管理中心的appid
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.ordinary_staff_app_list_of_my_tenant(staff_id=staff_id)
        data = endpoint(op)
        res = (op + data).ordinary_staff_app_list_of_my_tenant

        return [i["id"] for i in res.data if i["name"] == "管理中心"][0]

    def all_authorizations_of_user_api(self, staff_id):
        # 这个接口有鬼
        """
        查看所有权限
        @param staff_id:
        @return:
        """
        app_keys = self.ordinary_staff_app_list_of_my_tenant_api(staff_id)
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.all_authorizations_of_user(filter={"appKeys": app_keys,
                                              "isLeafOnly": True,
                                              "search": None},
                                      user_id=staff_id)
        data = endpoint(op)
        res = (op + data).all_authorizations_of_user

        return res

    def add_account_roles_api(self, input_data):
        """
        批量添加角色
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.add_account_roles(input=input_data)
        data = endpoint(op)
        res = (op + data).add_account_roles
        return res

    def remove_account_roles_api(self, input_data):
        """
        批量移除角色
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.remove_account_roles(input=input_data)
        data = endpoint(op)
        res = (op + data).remove_account_roles
        return res


if __name__ == '__main__':
    a = Account()

    # res = a.get_user("3d327a12-89d3-41b6-93e7-42b668d5e455")
    res = a.get_me()
    print(res)
