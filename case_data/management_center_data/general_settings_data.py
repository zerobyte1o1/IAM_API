from apis.base.base_api import BaseApi
from apis.management_center.general_settings_apis import GeneralSettings


class GeneralSettingsData(BaseApi):
    def get_oauth2_ask(self, id=None):
        """
        oauth认证的请求数据
        @param id: id为None时为创建参数，id有值时为修改参数
        @return: dict
        """
        args = list()
        variables_temp = self.get_variables(module_name="general_settings", variables_name="create_oauth2")
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
        variables_temp = self.get_variables(module_name="general_settings", variables_name="create_oidc1")
        if id is not None:
            args.append(("id", id))
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_login_config_to_my_tenant_data(self):
        args = list()
        variables_temp = self.get_variables(module_name="general_settings",
                                            variables_name="set_login_config_to_my_tenant")

        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = GeneralSettingsData()
    b = GeneralSettings()
    variables = a.set_login_config_to_my_tenant_data()
    res = b.set_login_config_to_my_tenant_api(variables)
    print(res)
