from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class MetaTemplate(GetTokenHeader):

    def get_meta_template_list(self):
        """
        查看所有推送模板
        @return: 返回所有推送模板
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.meta_template_list()
        data = endpoint(op)
        res = (op + data).meta_template_list
        return res

    def get_app_list(self):
        """
        获取所有拥有的app（接口有问题，目前只能获取部分）
        @return: 返回app数据
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.my_app_list()
        data = endpoint(op)
        res = (op + data).my_app_list
        return res.data

    def create_meta_template_api(self, variables):
        """
        创建推送模板
        @param variables:
        @return: template_id
        """
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
        """
        更新推送模板
        @param variables:
        @return:True or False
        """
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

    def overwrite_message_template_api(self, template_id):
        """
        更新模板
        @param template_id:
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.overwrite_message_template(id=template_id)
        data = endpoint(op)
        try:
            res = (op + data).overwrite_message_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_status_of_template_api(self, template_id, status):
        """
        更改模板状态
        @param template_id: 模板id
        @param status: 模板状态 ENABLED or DISABLED
        @return: Ture or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_status_of_template(id=template_id,
                                       status=status)
        data = endpoint(op)
        try:
            res = (op + data).update_status_of_template
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
    res = mt.get_app_list()
    print(res)
