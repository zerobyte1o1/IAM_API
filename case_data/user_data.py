from apis.base_api import BaseApi
from apis.user_apis import User
from utils.mock import Mock


class UserData(BaseApi):
    mock = Mock()
    u = User()
    role_name = mock.mock_data("role")
    role_id = u.roles_info().data[0].id

    def user_count(self):
        res = self.u.users_info(args=["total_count"])
        return res.total_count

    def role_count(self):
        res = self.u.roles_info(args=["total_count"])
        return res.total_count

    def create_role(self):
        variables_temp = self.get_variables(module_name="user", variables_name="create_role")
        args = [("name", self.role_name)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_user(self):
        user_account = self.mock.mock_data("account")
        user_name = self.mock.mock_data("name")
        variables_temp = self.get_variables(module_name="user", variables_name="create_user")
        args = [("account", user_account), ("name", user_name), ("role", [{"id": self.role_id}])]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    s = UserData()
    print(s.create_user())
