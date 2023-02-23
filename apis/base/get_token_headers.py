from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.base_api import BaseApi
from schema.platform_schema import Mutation


class GetTokenHeader(BaseApi):
    def __init__(self, **kwargs):
        super().__init__()
        if kwargs:
            self.headers = self.get_headers(account=kwargs["account"],
                                            password=kwargs["password"],
                                            tenant_code=kwargs["tenant_code"])
        else:
            self.headers = self.get_headers()

    def get_token(self, account=BaseApi.account, password=BaseApi.password, tenant_code=BaseApi.tenant_code):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": account,
            "password": password,
            "tenantCode": tenant_code
        }
        op = Operation(Mutation)
        login = op.login(input=variables)
        login.token()
        data = endpoint(op)
        res = (op + data).login
        token = "Token " + res.token
        return token

    def get_headers(self, account=BaseApi.account, password=BaseApi.password, tenant_code=BaseApi.tenant_code):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        headers.setdefault("authorization", self.get_token(account, password, tenant_code))
        return headers


if __name__ == '__main__':
    a = GetTokenHeader()
    res = a.get_headers()
    print(res)
