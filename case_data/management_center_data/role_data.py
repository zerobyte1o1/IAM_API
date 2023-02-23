from apis.base.base_api import BaseApi
from apis.management_center.role_apis import Role
from case_data.management_center_data.account_data import AccountData
from apis.management_center.account_apis import Account
from utils.mock import Mock


class RoleData(BaseApi):
    def __init__(self, **kwargs):
        self.role = Role(**kwargs)
        self.mock = Mock(**kwargs)
        self.account = Account()
        self.role_name = self.mock.mock_data("role")
        self.account_data = AccountData(**kwargs)

    def role_count(self):
        """
        计算现有角色数量
        @return: [int] 角色数量
        """
        res = self.role.get_role_list(args=["total_count"])
        return res.total_count

    def create_role_ask(self):
        """"""
        args = list()
        variables_temp = self.get_variables(module_name="role", variables_name="create_role")
        args.append(("name", self.role_name))
        args.append(("description", self.faker.text(max_nb_chars=20)))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_role_ask(self, role_id):
        """

        @param role_id: 被修改的角色id
        @return:  [dict] 更新请求数据
        """
        args = list()
        variables_temp = self.get_variables(module_name="role", variables_name="update_role")
        args.append(("name", self.role_name))
        args.append(("description", self.faker.text(max_nb_chars=20)))
        args.append(("id", role_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_authorization_rules_to_role_data(self, roleId):
        """
        为角色添加一个权限
        @param roleId:角色id
        @return : 只有一条权限的角色配置权限variables
        """
        args = list()
        filter_data = {
            "permissionTypes": [
                "PAGE",
                "MENU"
            ]
        }
        authorizationRules = self.role.all_authorization_roles_of_role_api(["permission", "id", "is_allowed"],
                                                                filter=filter_data,
                                                                role_id=roleId)
        variables_temp = self.get_variables(module_name="role", variables_name="set_authorization_rules_to_user")
        args.append(("authorizationRules", authorizationRules))
        args.append(("role", {"id": roleId}))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_role_accounts_data(self, role_id):
        """
        所有账号与一个角色
        @param role_id:
        @return:
        """
        args = list()
        account_list_data = self.account_data.account_list_filter()
        account_list = self.account.get_account_list(account_list_data).data
        variables_temp = self.get_variables(module_name="role", variables_name="set_role_accounts")
        args.append(("accountIds", [i["id"] for i in account_list]))
        args.append(("roleId", role_id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':

    for i in range(1):
        b = Role()
        a = RoleData()
        data = a.set_authorization_rules_to_role_data("736f5948-f10a-4e6b-9f37-b086674c1b4e")
        print(data)
