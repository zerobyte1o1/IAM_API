from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Company(GetTokenHeader):

    def get_admin_account_list(self):
        """
        获取管理员列表
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.admin_account_list()
        data = endpoint(op)
        res = (op + data).admin_account_list
        return res

    def set_admin_users_api(self, ids):
        """
        设置普通用户为管理员
        @param ids:[list]
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_admin_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).set_admin_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def unset_admin_users_api(self, ids):
        """
        移除管理员
        @param ids:[list]
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.unset_admin_users(ids=ids)
        data = endpoint(op)
        try:
            res = (op + data).unset_admin_users
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def transfer_tenant_owner_api(self, targetUserId):
        """
        转移企业拥有者
        @param targetUserId:
        @return:True or False
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.transfer_tenant_owner(target_user_id=targetUserId)
        data = endpoint(op)
        try:
            res = (op + data).transfer_tenant_owner
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def upload_config_api(self, img_name):
        """
        获取图片存储配置
        @param img_name:图片名称
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.upload_config(name=img_name)
        data = endpoint(op)
        try:
            res = (op + data).upload_config
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_image_api(self, compress_img_name):
        """
        创建图片存储地址
        @param compress_img_name:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_image(input={"name": compress_img_name})
        data = endpoint(op)
        try:
            res = (op + data).create_image
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res

    def apply_for_tenant_certification_api(self, img_id):
        """
        申请租户认证
        @id:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.apply_for_tenant_certification(input={"businessLicenseImage":{"id":img_id}})
        data = endpoint(op)
        try:
            res = (op + data).apply_for_tenant_certification
            return res
        except:
            res = data.get("errors")[0].get("message")
        return res


if __name__ == '__main__':
    a = Company(account="owner_NTHMps",password="zlyy728fgpd5",tenant_code="90123504")

    res=a.apply_for_tenant_certification_api(159)

    print(res)
