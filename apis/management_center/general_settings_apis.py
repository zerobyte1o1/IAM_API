from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class GeneralSettings(GetTokenHeader):
    def delete_authentication_configuration_api(self, id):
        """
        重置已有的认证设置
        @param id: 认证设置id
        @return: TRUE OR FALSE
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_authentication_configuration(id=id)
        data = endpoint(op)
        try:
            res = (op + data).delete_authentication_configuration
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def authentication_configuration_api(self):
        """
        查看当前企业的认证设置信息
        @return: 存在时返回基本信息，不存在时返回NULL
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.authentication_configuration()
        data = endpoint(op)
        res = (op + data).authentication_configuration
        return res

    def create_oauth2_authentication_configuration_api(self, variables):
        """
        创建oauth2.0的认证
        @param variables: 认证请求
        @return: id
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_oauth2_authentication_configuration(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_oauth2_authentication_configuration
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_open_idconnect1_authentication_configuration_api(self, variables):
        """
        创建OIDC1.0的认证
        @param variables: 认证请求
        @return: id
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_open_idconnect1_authentication_configuration(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_open_idconnect1_authentication_configuration
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_oauth2_authentication_configuration_api(self, variables):
        """
        更新oauth2.0认证设置
        @param variables: 修改请求数据
        @return:TRUE OR FALSE
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_oauth2_authentication_configuration(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_oauth2_authentication_configuration
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_open_idconnect1_authentication_configuration_api(self, variables):
        """
        更新OIDC1.0认证设置
        @param variables: 修改请求数据
        @return:TRUE OR FALSE
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_open_idconnect1_authentication_configuration(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_open_idconnect1_authentication_configuration
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def login_config_of_my_tenant_api(self):
        """
        当前企业通用配置基本信息
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.login_config_of_my_tenant()
        data = endpoint(op)
        res = (op + data).login_config_of_my_tenant
        return res

    def set_login_config_to_my_tenant_api(self,input_data):
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_login_config_to_my_tenant(input=input_data)
        data = endpoint(op)
        res = (op + data).set_login_config_to_my_tenant
        return res


if __name__ == '__main__':
    aut = GeneralSettings()
    # res = aut.delete_authentication_configuration_api("77ba4600-e252-4e3b-929d-5fc640fa0b53")
    # print(res)
    res = aut.delete_authentication_configuration_api("98a8c716-79a0-4e0a-ba82-3df3ca4f8a19")
    print(res)
