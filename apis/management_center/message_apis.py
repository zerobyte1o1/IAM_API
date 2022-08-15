from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.base.get_token_headers import GetTokenHeader
from schema.platform_schema import *


class Message(GetTokenHeader):
    def set_channels_of_message_template_api(self, variables):
        """
        编辑消息模板
        @param variables:
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_channels_of_message_template(channel_ids=variables["channelIds"],
                                            message_template_id=variables["messageTemplateId"],
                                            tenant_id=variables["tenantId"])
        data = endpoint(op)
        try:
            res = (op + data).set_channels_of_message_template
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def deactivate_message_channel_api(self,id):
        """
        取消开通媒介
        @param id: 媒介id
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.deactivate_message_channel(id=id)
        data = endpoint(op)
        try:
            res = (op + data).deactivate_message_channel
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res
        
    def active_message_channel_api(self,id):
        """
        开通媒介
        @param id: 媒介id
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.active_message_channel(id=id)
        data = endpoint(op)
        try:
            res = (op + data).active_message_channel
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def set_channel_of_message_templates_api(self,variables):
        """
        设置媒介模板
        @param variables:
        @return: True or False
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=self.headers)
        op = Operation(Mutation)
        op.set_channel_of_message_templates(channel_id=variables["channelId"],
                                            message_template_ids=variables["messageTemplateIds"],
                                            tenant_id=variables["tenantId"])

        data = endpoint(op)
        try:
            res = (op + data).set_channel_of_message_templates
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res