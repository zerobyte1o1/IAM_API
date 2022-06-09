from apis.base.base_api import BaseApi
from apis.management_center.role_apis import Role
from case_data.user_data import UserData
from apis.management_center.user_apis import User
from utils.mock import Mock


class RoleData(BaseApi):
    role = Role()
    mock = Mock()
    user = User()
    role_name = mock.mock_data("role")
    userdata = UserData()

    def role_count(self):
        res = self.role.get_role_list(args=["total_count"])
        return res.total_count

    def create_role_ask(self):
        """"""
        variables_temp = self.get_variables(module_name="role", variables_name="create_role")
        args = [("name", self.role_name), ("description", self.faker.text(max_nb_chars=20))]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_role_ask(self, role_id):
        """

        @param role_id: 被修改的角色id
        @return:
        """
        variables_temp = self.get_variables(module_name="role", variables_name="update_role")
        args = [("name", self.role_name), ("description", self.faker.text(max_nb_chars=20)), ("id", id)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_authorization_rules_to_role(self, roleId):
        """
        为角色添加一个权限
        @param roleId:角色id
        @return : 只有一条权限的角色配置权限variables
        """
        user_Id = self.user.get_me().id
        rule_id = self.userdata.get_one_permissions_of_user(user_Id)
        variables_temp = self.get_variables(module_name="role", variables_name="set_authorization_rules_to_user")
        args = [
            ("authorizationRules",
             [{"dataRange": {"code": "ALL", "name": "全部数据"}, "permission": {"id": rule_id}, "isAllowed": True}]),
            ("role", {"id": roleId})
        ]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = RoleData().set_authorization_rules_to_role("4ef43438-50fa-4b15-9036-f742aa370fce")
    print(a)
