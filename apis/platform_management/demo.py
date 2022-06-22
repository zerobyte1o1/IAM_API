from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Demo(GetTokenHeader):
    def get_countries(self):
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.countries(filter={'full': None})
        data = endpoint(op)
        res = (op + data).countries
        return res

    def get_department(self):
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.Department(filter={'full': None})
        data = endpoint(op)
        res = (op + data).department
        return res
if __name__ == '__main__':
    td=Demo()
    res=td.get_department()
    print(res)