from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MetaTemplate(GetTokenHeader):

    def get_meta_template_list(self, ):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.meta_template_list()
        data = endpoint(op)
        res = (op + data).meta_template_list
        return res

    def create_meta_template_ask(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_meta_template(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_meta_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_meta_template_api(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_meta_template(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_meta_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def over_write_message_template_api(self, template_id):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.over_write_message_template(id=template_id)
        data = endpoint(op)
        try:
            res = (op + data).over_write_message_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_status_of_template_api(self, template_id, status):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.over_write_message_template(id=template_id,
                                       status=status)
        data = endpoint(op)
        try:
            res = (op + data).over_write_message_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_meta_template_api(self, template_id):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_meta_template(id=template_id)
        data = endpoint(op)
        try:
            res = (op + data).delete_meta_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    mt = MetaTemplate()
    res = mt.get_meta_template_list()
    print(res)
