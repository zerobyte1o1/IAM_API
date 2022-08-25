from apis.base.base_api import BaseApi
from apis.management_center.account_apis import Account
from apis.management_center.organization_apis import Organization
from apis.management_center.role_apis import Role


class AccountData(BaseApi):
    def __init__(self, **kwargs):
        self.u = Account(**kwargs)
        self.role = Role(**kwargs)
        self.org = Organization(**kwargs)
        # org_id = org.get_organization_tree_nodes()[0]["id"]
        self.role_id = self.role.get_role_list().data[0].id

    def account_list_filter(self, search=None, roles=None):
        """

        @param search: 关键字查询，默认无
        @param roles: 角色筛选,默认无
        @return:
        """
        variables_temp = self.get_variables(module_name="account", variables_name="account_list")
        args = list()
        if search is not None:
            args.append(("search", search))
        if roles is not None:
            args.append(("roles", roles))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_account_data(self, account_id, isAllowedToLogin=None):
        """

        @param account_id: 账号id
        @param isAllowedToLogin: 是否允许登录
        @return:
        """
        args = list()
        variables_temp = self.get_variables(module_name="account", variables_name="update_account")
        args.append(("id", account_id))
        args.append(("role", [{"id": self.role_id}]))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def get_direct_authorization_rules_id_of_user(self, userId):
        """
        获取用户的所有已添加的权限规则id
        @param userId:用户id
        @return : 用户拥有的所有权限id集合,['d215d4e7-515b-4e27-a0c5-7254423f2fd8', '43970533-2b57-4d40-8543-d57219ac4695']
        """
        ids_list = []
        res = self.u.get_direct_authorization_rules_of_user(args=["id"], kwargs={
            "filter": {
                "permissionTypes": [
                    "PAGE"
                ]
            },
            "userId": userId
        })
        for ar in res.data:
            ids_list.append(ar["id"])
        return ids_list

    def get_one_permissions_of_user(self):
        """
        获取一个用户能够添加的权限规则的id
        @return 获取一个用户能获取范围内的权限id
        """
        user_Id = self.u.get_me().id
        res = self.u.get_all_permissions_of_user(args=["dependencies", "id"], kwargs={
            "filter": {
                "types": [
                    "MENU",
                    "PAGE"
                ]
            },
            "userId": user_Id
        })
        # 确保规则含有dependencies，否则updata规则时会出现参数缺失情况
        for i in range(len(res)):
            if res[i]["dependencies"]:
                return res[i]["id"]

    def set_authorization_rules_to_user(self, userId):
        """
        为user添加一个权限
        @param userId:用户id
        @return : 只有一条权限的用户配置权限variables
        """
        rule_id = self.get_one_permissions_of_user()

        variables_temp = self.get_variables(module_name="account", variables_name="set_authorization_rules_to_user")
        args = [
            ("authorizationRules",
             [{"dataRange": {"code": "ALL", "name": "全部数据"}, "permission": {"id": rule_id}, "isAllowed": True}]),
            ("user", {"id": userId})
        ]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_authorization_rules_of_user(self, userId):
        """
        获取用户已添加规则的单条数据并转换为请求格式
        @param userId: 用户的id
        @return: updata用户请求数据
        """
        data_tange = []
        rule_id = self.get_direct_authorization_rules_id_of_user(userId)[0]
        data = self.u.get_authorization_rule_and_dependencies(rule_id)
        for i in range(len(data)):
            data_tange.append({
                "dataRange": {
                    "code": data[i].data_range["code"],
                    "name": data[i].data_range["name"]
                },
                "id": data[i].id
            })
        variables = {"authorizationRules": data_tange, "user": {"id": userId}}
        return variables

    def add_and_remove_account_roles_data(self,account_id):
        args = list()
        list_data = self.account_list_filter()
        roles = self.role.get_role_list().data
        variables_temp = self.get_variables(module_name="account", variables_name="add_account_roles")
        args.append(("accountIds", [account_id]))
        args.append(("roleIds", [i["id"] for i in roles]))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = AccountData()
    b = Account()

    data = a.add_and_remove_account_roles_data()
    res=b.remove_account_roles_api(data)
    print(res)
