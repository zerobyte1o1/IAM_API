from apis.base.base_api import BaseApi
from apis.management_center.authentication_apis import Authentication


class AuthenticationData(BaseApi):
    def get_oauth2_ask(self, id=None):
        """
        oauth认证的请求数据
        @param id: id为None时为创建参数，id有值时为修改参数
        @return: dict
        """
        args = list()
        variables_temp = self.get_variables(module_name="authentication", variables_name="create_oauth2")
        if id is not None:
            args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def get_oidc1_ask(self, id=None):
        """
        oidc的请求数据
        @param id: d: id为None时为创建参数，id有值时为修改参数
        @return: dict
        """
        args = list()
        variables_temp = self.get_variables(module_name="authentication", variables_name="create_oidc1")
        if id is not None:
            args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = AuthenticationData()
    b = Authentication()
    variables = a.get_oauth2_ask('6dd0f275-f820-46bf-8c7b-467b724381c5')
    res = b.update_oauth2_authentication_configuration_api(variables)
    print(res)
