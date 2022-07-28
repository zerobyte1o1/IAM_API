from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Staff(GetTokenHeader):

    def get_staff_list(self, filter_data):
        """
        获取人员列表
        @param filter_data: staff_list_data
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Query)
        op.staff_list(filter=filter_data)
        data = endpoint(op)
        res = (op + data).staff_list
        return res

    def create_staff_apis(self, input_data):
        """
        创建人员
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.create_staff(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).create_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_staff_apis(self,input_data):
        """
        更新人员信息
        @param input_data:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.update_staff(input=input_data)
        data = endpoint(op)
        try:
            res = (op + data).update_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_staff_apis(self,staff_ids):
        """
        删除人员
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.delete_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).delete_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def hire_staff_apis(self,staff_ids):
        """
        办理入职
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.hire_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).hire_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def resign_staff_apis(self,staff_ids):
        """
        办理离职
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.resign_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).resign_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def rehire_staff_apis(self,staff_ids):
        """
        办理重新入职
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.rehire_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).rehire_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def archive_staff_apis(self,staff_ids):
        """
        归档人员
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.archive_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).archive_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def restore_staff_apis(self,staff_ids):
        """
        恢复人员
        @param staff_ids:
        @return:
        """
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.restore_staff(ids=[staff_ids])
        data = endpoint(op)
        try:
            res = (op + data).restore_staff
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res