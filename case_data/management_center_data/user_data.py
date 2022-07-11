from apis.base.base_api import BaseApi
from apis.management_center.user_apis import User
from apis.management_center.organization_apis import Organization
from apis.management_center.role_apis import Role
from utils.mock import Mock


class UserData(BaseApi):
    mock = Mock()
    u = User()
    role = Role()
    org = Organization()
    org_id = org.get_organization_tree_nodes()[0]["id"]
    role_id = role.get_role_list().data[0].id

    def user_list_filter(self, org_ids, include_children_organizations=None, include_disabled_users=None):
        """
        @param include_disabled_users: [booleam]是否需要包括禁用用户
        @param include_children_organizations: [booleam]是否需要包括子组织的user
        @param org_ids: 组织id
        """
        variables_temp = self.get_variables(module_name="user", variables_name="user_list")
        args = [("organizations", org_ids)]
        if include_children_organizations is not None:
            args.append(("includeChildrenOrganizations", include_children_organizations))
        if include_disabled_users is not None:
            args.append(("includeDisabledUsers", include_disabled_users))

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_user(self):
        user_account = self.mock.mock_data("account")
        user_name = self.mock.mock_data("name")
        variables_temp = self.get_variables(module_name="user", variables_name="create_user")

        args = [("account", user_account),
                ("name", user_name),
                ("organizations", [{"id": self.org_id}])
                ]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_user(self, userId):
        """
        @param userId:被修改用户的id
        @return ：修改了name和roles的variables
        """
        user_id = userId
        user_name = self.mock.mock_data("name")
        fake_email = self.faker.email()
        fake_phone = self.faker.phone_number()
        fake_remark = self.faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        variables_temp = self.get_variables(module_name="user", variables_name="update_user")
        args = [("id", user_id),
                ("name", user_name),
                ("email", fake_email),
                ("phoneNumber", fake_phone),
                ("remark", fake_remark),
                ("organizations", [{"id": self.org_id}])
                ]
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

        variables_temp = self.get_variables(module_name="user", variables_name="set_authorization_rules_to_user")
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


if __name__ == '__main__':
    # s = UserData()
    # print(s.create_user())
    a = UserData()

    # data = UserData().get_direct_authorization_rules_id_of_user("3fffa3c1-ca9d-4455-b133-8a2fbb8ecb38")
    # print(data)
    # res = a.set_authorization_rules_to_user_api(data)
    # print(res)
    # data = UserData().update_authorization_rules_of_user("0c84960e-d04c-4c2d-9bc3-62eb860633ba")
    # print(data)
    # res = a.update_authorization_rules_of_user_api(data)
    res=a.create_user()
    print(res)
