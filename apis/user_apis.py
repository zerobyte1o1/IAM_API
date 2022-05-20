from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Mutation, Query


class User(GetTokenHeader):
    def get_user(self):
        """
        :return:class User; 如果想要company_id, 可以使用:
            res.company.id, res = return
        """
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.me()
        data = endpoint(op)
        res = (op + data).me
        return res

    def users_info(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.users(
            filter=eval(f"{kwargs}"),
        )
        if args:
            users_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).users
        return res

    def roles_info(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.role_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            users_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).role_list
        return res

    def create_user(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_role(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    a = User()
    # res1 = a.get_user()
    # print(res1.company.id)
    # res2 = a.get_headers(account="admin", password="teletraan@2022")
    res2 = a.roles_info().data[0].id
    print(res2)
