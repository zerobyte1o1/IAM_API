from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import Mutation, Query


class User(GetTokenHeader):
    def get_me(self):
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

    def get_user(self, id):
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.user(id=id)
        data = endpoint(op)
        res = (op + data).user
        return res

    def roles_info(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.role_list(
            filter=eval(f"{kwargs}")
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

    def get_user_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        user_list = op.user_list(filter=eval(f"{kwargs}"))
        if args:
            user_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).user_list
        return res

    def enable_users(self, ids):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.enable_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).enable_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def disable_users(self, ids):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.disable_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).disable_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_users(self, ids):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).delete_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def reset_user_password(self, id):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.reset_user_password(id=id)
        data = endpoint(op)
        try:
            res = (op + data).reset_user_password
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_user(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    a = User()
    # res1 = a.get_user()
    # print(res1.company.id)
    # res2 = a.get_headers(account="admin", password="teletraan@2022")
    # request_data = {
    #     "includeChildrenOrganizations": "true",
    #     "includeDisabledUsers": "true",
    #     "isAdmin": "false",
    #     "organizations": [
    #         {
    #             "id": "a1c97533-4149-4a13-bf73-e4a3bf08a25a"
    #         }
    #     ],
    #     "search": ""
    # }
    # res = a.get_user_list(args=["data"], kwargs=request_data)

    #print(res)
