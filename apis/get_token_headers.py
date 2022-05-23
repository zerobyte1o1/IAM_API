from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base_api import BaseApi
from schema.platform_schema import Mutation


class GetTokenHeader(BaseApi):
    def get_token(self, account=BaseApi.account, password=BaseApi.password, tenantCode=BaseApi.tenantCode):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": account,
            "password": password,
            "tenantCode":tenantCode
        }
        op = Operation(Mutation)
        login = op.login(input=variables)
        login.token()
        data = endpoint(op)
        res = (op + data).login
        token = "Token " + res.token
        return token

    def get_headers(self, account=BaseApi.account, password=BaseApi.password,tenantCode=BaseApi.tenantCode):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        headers.setdefault("authorization", self.get_token(account, password,tenantCode))
        return headers
